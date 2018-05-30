#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "bs4",
    "html5lib",
    "textstat",
    "nltk",
    "language_check",
    "textblob",
    "langdetect",
    "urllib3",
    "certifi"
]

setup_requirements = [
]

test_requirements = [
]

setup(
    author="Ashley Williams",
    author_email='ashley.williams@pg.canterbury.ac.nz',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Core functionality of COAST",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='coast_core',
    name='coast_core',
    packages=find_packages(include=['coast_core']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/zedrem/coast_core',
    version='0.1.0',
    zip_safe=False,
)
