#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of pyopenlibrary, a Python Interface to the Open Library.
# Copyright © 2013 Kali Kaneko, <kali@futeisha.org>
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the included LICENSE file for details.
#______________________________________________________________________________

from __future__ import absolute_import
from __future__ import print_function

import setuptools


__version__ = "0.0.1"
__author__ = "Kali Kaneko"
__contact__ = 'kali@futeisha.org'
__url__ = 'https://github.com/kalikaneko/pyopenlibrary'

requires = ["requests"]

setuptools.setup(
    name="openlibrary",
    description="A Python Interface for the OpenLibrary API",
    long_description="""\
Allow book searches using the Open Library API.
""",
    license="GPLv3+",
    version=__version__,
    author=__author__,
    author_email=__contact__,
    maintainer=__author__,
    maintainer_email=__contact__,
    url=__url__,
    py_modules=['openlibrary'],
    package_data={'': ['README', 'LICENSE']},
    platforms="Linux, BSD, OSX, Windows",
    download_url="https://github.com/kalikaneko/pyopenlibrary/archive/master.zip",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities", ]
)
