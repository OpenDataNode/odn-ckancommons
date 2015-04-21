'''
@author: jmc
'''
from setuptools import setup, find_packages

version = '0.5.1-SNAPSHOT'

setup(
    name='odn-ckancommons',
    version=version,
    description="""
    CKAN's commons for development of ODN related extensions
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
    namespace_packages=['odn_ckancommons'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        ''
    ],
)
