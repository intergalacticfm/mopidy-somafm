from __future__ import unicode_literals

import re
from setuptools import setup, find_packages


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='Mopidy-SomaFM',
    version=get_version('mopidy_somafm/__init__.py'),
    url='http://github.com/AlexandrePTJ/mopidy-somafm/',
    license='MIT License',
    author='Alexandre Petitjean',
    author_email='alpetitjean@gmail.com',
    description='SomaFM extension for Mopidy',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy',
        'requests',
    ],
    entry_points={
        'mopidy.ext': [
            'somafm = mopidy_somafm:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)