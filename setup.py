#!/usr/bin/env python

from distutils.core import setup

setup(name='django-safehtmlform',
      version='1.0',
      description='Sanitized HTML form field',
      author='Jordan Reiter',
      author_email='jordanreiter@gmail.com',
      url='https://github.com/JordanReiter/django-safehtmlform',
      packages=['safehtmlform', 'safehtmlform.templatetags'],
     )