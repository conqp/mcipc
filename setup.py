#! /usr/bin/env python

from setuptools import setup

setup(
    name='mcipc',
    version_format='{tag}',
    setup_requires=['setuptools-git-version'],
    author='Richard Neumann',
    author_email='<mail at richard dash neumann dot de>',
    python_requires='>=3.6',
    packages=[
        'mcipc',
        'mcipc.query',
        'mcipc.query.proto',
        'mcipc.rcon',
        'mcipc.rcon.datastructures'],
    scripts=['files/rconclt', 'files/rconshell'],
    url='https://github.com/conqp/mcipc',
    license='GPLv3',
    description='A Minecraft server inter-process communication library.')
