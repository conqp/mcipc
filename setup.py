#! /usr/bin/env python
"""Installation script."""

from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

setup(
    name='mcipc',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author='Richard Neumann',
    author_email='mail@richard-neumann.de',
    python_requires='>=3.9',
    packages=[
        'mcipc',
        'mcipc.query',
        'mcipc.query.proto',
        'mcipc.rcon',
        'mcipc.rcon.be',
        'mcipc.rcon.be.commands',
        'mcipc.rcon.commands',
        'mcipc.rcon.ee',
        'mcipc.rcon.ee.commands',
        'mcipc.rcon.je',
        'mcipc.rcon.je.commands',
        'mcipc.rcon.response_types',
        'mcipc.server'
    ],
    install_requires=['rcon'],
    entry_points={
        'console_scripts': [
            'mcstubsrv = mcipc.server.stubsrv:main',
            'queryclt = mcipc.query.queryclt:main'
        ],
    },
    url='https://github.com/conqp/mcipc',
    license='GPLv3',
    description='A Minecraft server inter-process communication library.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='minecraft python server rcon query'
)
