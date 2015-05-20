#!/usr/bin/env python
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import json_loader


class Tox(TestCommand):
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args)
        sys.exit(errno)

setup(
    name='json-loader',
    author='Eugeny Volobuev',
    author_email='quert@gmail.com',
    version=json_loader.__version__,
    url='http://github.com/jintwo/python-json-loader',
    packages=find_packages(),
    tests_require=['pytest', 'tox'],
    cmdclass={'test': Tox})
