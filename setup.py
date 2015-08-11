try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(name='Balert',
      version='0.1dev',
      install_requires=[
          r for r in open('requirements.txt', 'r').read().split('\n') if r],
      author='Tushar Gautam',
      author_email='tushar.rishav@gmail.com',
      packages=['balert',],
      entry_points={
          'console_scripts': ['balert=balert:main'],
      },
      url='https://github.com/tushar-rishav/balert/',
      description='A speaking battery status manager',
      long_description=open('README.txt').read(),
      license=open('LICENSE.txt').read(),
      keywords=['reminder', 'battery', 'voice alert', 'python'],
      classifiers=[
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Topic :: Utilities'
      ],
      )