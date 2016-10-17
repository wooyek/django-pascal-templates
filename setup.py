# coding=utf-8
# Copyright 2014 Janusz Skonieczny
import sys
import os
import uuid
from setuptools import setup, find_packages
from pip.req import parse_requirements

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.join(ROOT_DIR, 'src')
sys.path.append(SRC_DIR)

install_requires = parse_requirements(
    os.path.join(os.path.dirname(__file__), "requirements.txt"),
    session=uuid.uuid1()
)
with open("README.rst", encoding="UTF-8") as readme:
    long_description = readme.read()

version = "0.8.10"

setup_kwargs = {
    'name': "django-pascal-templates",
    'version': version,
    'packages': find_packages("src", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    'package_dir': {'': 'src'},
    'install_requires': [str(r.req) for r in install_requires],

    # "package_data": {
    #     '': ['requirements.txt']
    # },

    'author': "Janusz Skonieczny",
    'author_email': "js+pypi@bravelabs.pl",
    'description': "Django generic views with PascalCase template paths with model named folders.",
    'long_description': long_description,
    'license': "MIT",
    'keywords': "django template folder dictionary pascal models",
    'url': "https://github.com/wooyek/django-pascal-templates",
    'classifiers': [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    'test_suite': 'pascal_templates.tests'
}

setup(**setup_kwargs)

