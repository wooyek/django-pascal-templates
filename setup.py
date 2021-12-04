# coding=utf-8
# Copyright 2014 Janusz Skonieczny
import io
from setuptools import find_packages, setup


with io.open("README.rst", encoding="UTF-8") as readme:
    long_description = readme.read()

version = "0.8.13"

setup_kwargs = {
    'name': "django-pascal-templates",
    'version': version,
    'packages': find_packages("src", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    'package_dir': {'': 'src'},
    'install_requires': ['Django>=1.8'],

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
