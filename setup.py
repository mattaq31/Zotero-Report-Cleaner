""" Setup script for package. """
from setuptools import setup, find_packages

setup(
    name="Zotero Report Cleaner",
    author="Matthew Aquilina",
    description="Package for streamlining Zotero Reports",
    url="https://github.com/mattaq31/Zotero-Report-Editor",
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        zotero_clean=main:convert
    ''',
)

