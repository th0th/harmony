# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='Harmony',
    version='0.1',
    author='H. Gökhan Sarı',
    author_email='th0th@returnfalse.net',
    packages=['harmony'],
    scripts=['bin/harmony'],
    url='https://github.com/th0th/harmony/',
    license='LICENSE.txt',
    description='Music folder organizer.',
    long_description=open('README.asciidoc').read(),
)
