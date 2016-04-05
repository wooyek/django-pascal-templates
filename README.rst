django-pascal-templates
=======================

Django generic views with PascalCase template paths with model named folders.

https://github.com/wooyek/django-pascal-templates

.. image:: https://img.shields.io/travis/wooyek/django-pascal-templates.svg   
   :target: https://travis-ci.org/wooyek/django-pascal-templates

.. image:: https://img.shields.io/coveralls/wooyek/django-pascal-templates.svg   
   :target: https://coveralls.io/github/wooyek/django-pascal-templates

Usage
-----

Replace your usual generic view imports with:

.. code:: python

   from pascal_templates.views import DetailView, CreateView, UpdateView, DeleteView, ListView

And in result get additional template_names allowing you to keep templates in folders named after your models:

.. code:: python

   names = [
      'some_app/somemodel_detail.html',
      'some_app/SomeModel/detail.html',   # This is what you get
    ]
