#!/usr/bin/env python
import os
import glob
from distutils.core import setup

def get_dir(d):
    return glob.glob('%s/*' % d)


ldesc = """IdleX is a collection of over 20 extensions for the Python IDLE environment."""

setup(name='idlexl',
      version='1.0',
      description='IDLE Extensions for Python3.6+',
      author='Wolfgang Maier',
      author_email='wolfgang.maier@biologie.uni-freiburg.de',
      url='https://github.com/wm75/idlexl',
      packages=['idlexl',
                'idlexl.extensions'],
      package_dir = {'idlexlib': 'idlexlib'},
      scripts = get_dir('scripts'),
      license='GPL',
      long_description=ldesc,
      classifiers = [
          'Development Status :: 5 - Production/Stable',
          'Framework :: IDLE',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'License :: OSI Approved :: Python Software Foundation License',
          'Topic :: Text Editors :: Integrated Development Environments (IDE)',
          'Operating System :: OS Independent',
        ],
     )
