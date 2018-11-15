synthqc
=======

[![Build Status](https://travis-ci.org/jcreinhold/synthqc.svg?branch=master)](https://travis-ci.org/jcreinhold/synthqc)
[![Coverage Status](https://coveralls.io/repos/github/jcreinhold/synthqc/badge.svg?branch=master)](https://coveralls.io/github/jcreinhold/synthqc?branch=master)
[![Documentation Status](https://readthedocs.org/projects/synthqc/badge/?version=latest)](http://synthqc.readthedocs.io/en/latest/?badge=latest)
[![Docker Automated Build](https://img.shields.io/docker/build/jcreinhold/synthqc.svg)](https://hub.docker.com/r/jcreinhold/synthqc/)
[![Python Versions](https://img.shields.io/badge/python-3.6%20%7C%203.7-blue.svg)](https://www.python.org/downloads/release/python-360/)

This package supports a suite of quality analysis programs for MR/CT image synthesis.

We also support a DNN-based and non-DNN-based synthesis package called [synthnn](https://gitlab.com/jcreinhold/synthnn) 
and [synthit](https://gitlab.com/jcreinhold/synthit), respectively.

** Note that this is an **alpha** release. If you have feedback or problems, please submit an issue (it is very appreciated) **

This package was developed by [Jacob Reinhold](https://jcreinhold.github.io) and the other students and researchers of the 
[Image Analysis and Communication Lab (IACL)](http://iacl.ece.jhu.edu/index.php/Main_Page).

[Link to main Gitlab Repository](https://gitlab.com/jcreinhold/synthit)

Requirements
------------

- matplotlib
- nibabel
- numpy
- scikit-image

Installation
------------

    pip install git+git://github.com/jcreinhold/synthqc.git

Tutorial
--------

[5 minute Overview](https://github.com/jcreinhold/synthqc/blob/master/tutorials/5min_tutorial.md)

   
Test Package
------------

Unit tests can be run from the main directory as follows:

    nosetests -v tests

