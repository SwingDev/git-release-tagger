#!/usr/bin/env python

import os
import re
import sys

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel upload')
    sys.exit()

packages = [
    'requests',
    'requests.packages',
    'requests.packages.chardet',
    'requests.packages.urllib3',
    'requests.packages.urllib3.packages',
    'requests.packages.urllib3.contrib',
    'requests.packages.urllib3.util',
    'requests.packages.urllib3.packages.ssl_match_hostname',
]

version = ''
with open('git_release_tagger/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name='git-release-tagger',
    version=version,
    author='Tomek Kopczuk',
    author_email='tkopczuk@gmail.com',
    packages=['git_release_tagger'],
    scripts=['bin/tag-release'],
    url='https://github.com/SwingDev/git-release-tagger',
    license='LICENSE',
    description='Small CLI utility to enable the CI environment to communicate the deployment progress through the use of git tags.',
    long_description=readme + '\n\n' + history,
    install_requires=[
        "argparse >= 1.4.0",
        "envoy >= 0.0.3"
    ],
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    )
)
