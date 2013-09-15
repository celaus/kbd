#!/usr/bin/python2

# KBD - A simple keyboard backlight daemon to control keyboard backlight with a web service
# Copyright (C) 2013  Claus Matzinger
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from setuptools import setup, find_packages

setup_dict = dict(
    name = "kbd",
    version = "1.0",
    author = 'Claus Matzinger',
    author_email = '',
    description = '',
    license = 'GPLv3',
    url = 'https://github.com/celaus/kbd',
    packages = find_packages('src'),
    package_dir = {'':'src'},
    entry_points = {  'run' : ["run = kbd.kbd:run"] },
    include_package_data = True,
    zip_safe = False,
)

setup(**setup_dict)
