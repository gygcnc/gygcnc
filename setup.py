#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import gygcnc
version = gygcnc.__version__

setup(
    name='gygcnc',
    version=version,
    author="diegoduncan21",
    author_email='diegoduncan21@gmail.com',
    packages=[
        'gygcnc',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.4',
    ],
    zip_safe=False,
    scripts=['gygcnc/manage.py'],
)
