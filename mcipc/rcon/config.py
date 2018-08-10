"""Server configuration parser."""

from mcipc.config import CredentialsConfig


__all__ = ['CONFIG']


CONFIG = CredentialsConfig('/etc/rcon.conf')
