#!/usr/bin/python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'Cryptopals',
        'url': 'https://github.com/wenchuan/cryptopals',
        'install_requires': ['nose'],
        'packages': ['cryptopals'],
        'scripts': [],
        'name': 'cryptopals'
}

setup(**config)
