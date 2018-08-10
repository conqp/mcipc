"""Query server configuration."""

from mcipc.config import CredentialsConfig


__all__ = ['CONFIG']


CONFIG = CredentialsConfig('/etc/mcipc.d/query.conf')
