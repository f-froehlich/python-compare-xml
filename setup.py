#!/usr/bin/python3
# -*- coding: utf-8

#  compare-xml
#
#  Comparator for XML Elements
#
#  Copyright (c) 2020 Fabian Fröhlich <compare-xml@f-froehlich.de> <https://projects.f-froehlich.de/compare-xml>
#
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#
#  Checkout this project on github <https://github.com/f-froehlich/compare-xml>
#  and also my other projects <https://github.com/f-froehlich>


from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()
with open('CHANGELOG.md') as changelog_file:
    CHANGELOG = changelog_file.read()
with open('CONTRIBUTORS.md') as changelog_file:
    CONTRIBUTORS = changelog_file.read()
with open('LICENSE') as changelog_file:
    LICENSE = changelog_file.read()

additional_files = [
    'README.md',
    'CHANGELOG.md',
    'CONTRIBUTORS.md',
    'LICENSE',
]
setup_args = dict(
    name='compare_xml',
    version='1.1.0',
    description='Comparator for XML Elements',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n\n' + CONTRIBUTORS + '\n\n\n' + CHANGELOG,
    license='AGPLv3',
    packages=find_packages(),
    author='Fabian Fröhlich',
    author_email='compare-xml@f-froehlich.de',
    maintainer='Fabian Fröhlich',
    maintainer_email='compare-xml@f-froehlich.de',
    keywords=['xml', 'compare'],
    download_url='https://github.com/f-froehlich/compare-xml',
    url='https://projects.f-froehlich.de/compare-xml',
    package_data={'compare_xml': additional_files},
)

install_requires = [
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
