from setuptools import setup, find_packages
import sys, os

version = '0.1.2'

setup(name='playstore',
      version=version,
      description="Python library to access Android App details from Google Play Store.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords=['Android', 'playstore'],
      author='Kracekumar',
      author_email='me@kracekumar.com',
      url='https://github.com/kracekumar/playstore',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
          'requests == 1.2.3',
          'beautifulsoup4'
      ],
      download_url = 'https://github.com/kracekumar/playstore/archive/v0.1.2.tar.gz',
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
