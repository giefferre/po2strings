# -*- coding: utf-8 -*-
"""
    po2strings
    ----------

    This utility helps you to localise your Apple or Android application.

    :author: Gianfranco Reppucci
    :copyright: (c) 2015 Qurami srl.
    :license: MIT, see LICENSE for more details.
"""

import re
import sys
import codecs
from os import path
from setuptools import setup, find_packages

VERSION = re.search("VERSION = '([^']+)'", codecs.open(
    path.join(path.dirname(__file__), 'po2strings', '__init__.py'),
    encoding="utf-8",
).read().strip()).group(1)

LONG_DESCRIPTION = open(path.join(path.dirname(__file__), 'README.rst')).read()

REQUIREMENTS = [
]

setup(
    name='po2strings',
    version=VERSION,
    url='http://qurami.com/',
    license='MIT',
    description='po2strings convert PO/POT files into Apple .strings or Android .xml locale files.',
    long_description=LONG_DESCRIPTION,
    author='Gianfranco Reppucci',
    author_email='gianfranco.reppucci@qurami.net',
    classifiers=[
        #'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=['po2strings'],
    package_data={},
    zip_safe=False,
    install_requires=REQUIREMENTS,
    entry_points={
        'console_scripts': [
            'po2strings = po2strings.__main__:main',
        ],
    },
)
