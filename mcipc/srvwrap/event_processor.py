"""Event processing."""

from logging import getLogger
from threading import Lock

from mcipc.srvwrap.common import Daemon
from mcipc.srvwrap.exceptions import CallbackExistsError
from mcipc.srvwrap.messages import MsgCancel


__all__ = ['EventProcessor']


LOGGER = getLogger(__file__)
DICT_LOCK = Lock()


class _RegisteredCallback:
    """Temporarily registers a callback."""

    def __init__(self, name, event_processor):
        """Sets callback and event processor."""
        self.name = name
        self.event_processor = event_processor

    def __enter__(self):
        """Registers the callback."""
        return self

    def __exit__(self, *_):
        """Cancels the callback."""
        self.event_processor.cancel(self.name)


class EventProcessor(Daemon):
    """Processes events."""

    def __init__(self, subprocess):
        """Sets subprocess and callbacks."""
        super().__init__()
        self.subprocess = subprocess
        self._callbacks = {}

    def _run(self):
        """Sets the subprocess and listens for events."""
        while self.subprocess.poll() is None:
            if self._terminate:
                break

            try:
                event = self.subprocess.stdout.readline()
            except KeyboardInterrupt:
                break

            with DICT_LOCK:
                callbacks = dict(self._callbacks)

            for name, handler in callbacks.items():
                try:
                    handler(event)
                except MsgCancel:
                    with DICT_LOCK:
                        self._callbacks.pop(name, None)
                except Exception as exception:  # pylint: disable=W0703
                    LOGGER.error(
                        'Event handler %s produced unhandled exception :%s.',
                        name, exception)

        self._thread = None

    def register(self, callback, name=None, override=False):
        """Registers a new callback function."""
        if name is None:
            name = callback.__name__

        if name in self._callbacks and not override:
            raise CallbackExistsError()

        with DICT_LOCK:
            self._callbacks[name] = callback

        return _RegisteredCallback(name, self)

    def cancel(self, callback_or_name):
        """Cancels the callback or name."""
        try:
            name = callback_or_name.__name__
        except AttributeError:
            name = str(callback_or_name)

        try:
            with DICT_LOCK:
                self._callbacks.pop(name)
        except KeyError:
            return False

        return True
