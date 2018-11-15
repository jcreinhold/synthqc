#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
setup

Module installs synthqc package
Can be run via command: python setup.py install (or develop)

Author: Jacob Reinhold (jacob.reinhold@jhu.edu)

Created on: Nov 15, 2018
"""

from setuptools import setup, find_packages
from sys import platform


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

args = dict(
    name='synthqc',
    version='0.1.0',
    description="Quality control/metrics for MR/CT synthesis",
    long_description=readme,
    author='Jacob Reinhold',
    author_email='jacob.reinhold@jhu.edu',
    url='https://gitlab.com/jcreinhold/synthqc',
    license=license,
    packages=find_packages(exclude=('tests', 'tutorials', 'docs')),
    entry_points = {
        'console_scripts': ['directory-view=synthqc.exec.directory_view:main',
                            'synth-quality=synthqc.exec.synth_quality:main',]
    },
    keywords="mr image synthesis quality",
)

setup(install_requires=['matplotlib',
                        'numpy',
                        'scikit-image',
                        'scipy'], **args)
