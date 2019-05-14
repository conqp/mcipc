#! /usr/bin/env python

import setuptools

setuptools.setup(
    name='mcipc',
    version='0.0.1',
    description="A Minecraft server inter-process communication library.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Richard Neumann',
    author_email='r.neumann@homeinfo.de',
    maintainer='Richard Neumann',
    maintainer_email='r.neumann@homeinfo.de',
    packages=[
        'mcipc',
        'mcipc.query',
        'mcipc.query.proto',
        'mcipc.rcon',
        'mcipc.rcon.datastructures'],
    scripts=['files/rconclt', 'files/rconshell'],
    url='https://github.com/conqp/mcipc',
    keywords='minecraft python server rcon query',
    license='GPLv3',
        classifiers=(
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux"
    ),
    python_requires='>=3.2',
    install_requires=[
        'docopt',
        'twine'
    ],
)
