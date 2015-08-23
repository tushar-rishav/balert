try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True
requirement_list = [r.strip() for r in open('requirements.txt', 'r').readlines() if r]
setup(name='Balert',
      version='1.0.4',
      install_requires=requirement_list,
      author='Tushar Gautam',
      author_email='tushar.rishav@gmail.com',
      packages=['balert', ],
      entry_points={
          'console_scripts': ['balert=balert:main'],
      },
      license='GNU General Public License v3 (GPLv3)',
      url='https://github.com/tushar-rishav/balert/',
      description="A speaking battery's charge level",
      long_description=open('README').read(),
      keywords=['reminder', 'battery', 'voice alert', 'python'],
      classifiers=[
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Topic :: System :: Monitoring'
      ],
      )