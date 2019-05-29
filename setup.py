#! /usr/bin/env python

import setuptools

setuptools.setup(
    name='mcipc',
    version='0.0.2',
    description="A Minecraft server inter-process communication library.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Richard Neumann',
    author_email='mail@richard-neumann.de',
    maintainer='Richard Neumann',
    maintainer_email='mail@richard-neumann.de',
    version_format='{tag}',
    setup_requires=['setuptools-git-version'],
    python_requires='>=3.6',
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
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux"
    ),
    install_requires=[
        'docopt',
        'twine'
    ],
)
