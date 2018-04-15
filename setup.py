#!/usr/bin/env python3

from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='mojang-api',
    version='2.1.0',
    description='A full Python wrapper of Mojang\'s API and Authentication API.',
    long_description=long_description,
    url='https://github.com/SynchronousX/mojang-api',
    author='Synchronous',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='mojang minecraft mc api authentication auth',
    packages=find_packages(),
    setup_requires='pytest-runner',
    tests_require=[
        'pytest',
        'pytest-cov'
    ],
    install_requires=[
        'python-box',
        'requests'
    ],
    python_requires='>=3.5.*'
)
