#! /usr/bin/env python

from distutils.core import setup

setup(
    name='mcipc',
    author='Richard Neumann',
    author_email='<mail at richard dash neumann dot de>',
    packages=['mcipc', 'mcipc.rcon', 'mcipc.query'],
    scripts=['files/rconclt', 'files/rconcmd'],
    url='https://github.com/conqp/mcipc',
    license='GPLv3',
    description='A Minecraft server inter-process communication library.')
