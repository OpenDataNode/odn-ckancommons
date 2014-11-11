'''
@author: jmc
'''
from setuptools import setup, find_packages

version = '0.1.0-SNAPSHOT'

setup(
    name='ckancommons',
    version=version,
    description="""
    Ckan's commons for development
    """,
    long_description="""
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Jan Marcek',
    author_email='jmc@eea.sk',
    url='',
    license='',
    packages=find_packages(exclude=['examples', 'tests']),
    namespace_packages=['ckancommons'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        ''
    ],
)
