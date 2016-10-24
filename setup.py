#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PgDbConn - Connect to Postgres database and issue commands
"""
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='pgdbconn',
    version='0.8.dev0',
    packages=['pgdbconn'],
    install_requires=['psycopg2 >= 2.5'],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    author='Joe Abbate',
    author_email='jma@freedomcircle.com',
    description='Object-oriented layer over Psycopg2 to connect and interact with Postgres databases',
    long_description=open('README.rst').read(),
    url='https://github.com/perseas/pgdbconn',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: SQL',
        'Topic :: Database :: Front-Ends'],
    platforms='OS-independent',
    license='BSD')
