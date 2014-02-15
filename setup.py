# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from asdf import __version__



setup(
    name='asdf',
    version=__version__,
    author='asdf',
    author_email='asdf',
    include_package_data = True,
    packages=find_packages(),
    description='asdf',
    url='asdf',   
    #long_description=open('README.rst').read(),
    #license='BSD License',
    #entry_points = {
    #    'console_scripts': ['asdf = asdf.cli:main'],
    #},
    install_requires=[
    
        ]
)