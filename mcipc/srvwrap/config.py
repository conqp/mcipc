"""Configuration parser."""

from configparser import ConfigParser


__all__ = ['CONFIG']


CONFIG = ConfigParser()
CONFIG.read('/etc/mcipc.d/srvwrap.conf')
