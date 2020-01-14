#! /usr/bin/env python

from setuptools import setup

setup(
    name='mcipc',
    version_format='{tag}',
    setup_requires=['setuptools-git-version'],
    author='Richard Neumann',
    author_email='mail@richard-neumann.de',
    python_requires='>=3.8',
    packages=[
        'mcipc',
        'mcipc.cli',
        'mcipc.query',
        'mcipc.query.proto',
        'mcipc.rcon',
        'mcipc.rcon.datastructures',
        'mcipc.server'],
    scripts=['files/queryclt', 'files/rconclt', 'files/rconshell'],
    url='https://github.com/conqp/mcipc',
    license='GPLv3',
    description='A Minecraft server inter-process communication library.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    keywords='minecraft python server rcon query'
)
