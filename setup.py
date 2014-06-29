#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='yoapi',
    version='1.0',
    description='Python YoApi.',
    long_description=readme,
    author='Brad Cowie',
    author_email='brad@gizmoguy.net.nz',
    url='http://github.com/gizmoguy/python-yoapi',
    packages=['yoapi'],
    install_requires=['requests'],
    license='Apache 2.0',
)
