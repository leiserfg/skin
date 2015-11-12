# -*- coding: utf-8 -*-
from setuptools import setup,find_packages
from skin import __version__

setup(
    name='skin',
    version=__version__,
    author='Leiser Ferández Gallo',
    author_email='leiserfg@gmail.com',
    include_package_data = True,
    packages=find_packages(),
    description='a simple static template render',
    long_description=open('README.md').read(),
    license='BSD License',
    url='https://github.com/leiserfg/skin/',
    entry_points = {
        'console_scripts': ['skin = skin.cli:main'],
    },
)
