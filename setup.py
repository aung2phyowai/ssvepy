from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

readme = 'A package that provides classes for SSVEP analysis'
if path.isfile('README.md'):
    readme = open('README.md', 'r').read()

version = '0.1.dev0'

setup(
    name='ssvepy',
    version=version,
    description='A package that provides classes for SSVEP analysis',
    long_description=readme,
    url='https://github.com/janfreyberg/ssvepy',
    download_url='https://github.com/janfreyberg/ssvepy' +
        version,
    author='Jan Freyberg',
    author_email='jan.freyberg@gmail.com',
    packages=['ssvepy'],
    install_requires=['mne', 'numpy', 'matplotlib'],
    package_data={
        '': ['exampledata/*fif']
    },
)
