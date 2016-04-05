django-pascal-templates
=======================

Django generic views with PascalCase template paths with model named folders.

https://github.com/wooyek/django-pascal-templates

.. image:: https://travis-ci.org/wooyek/django-pascal-templates.svg

.. image:: https://coveralls.io/repos/wooyek/django-pascal-templates/badge.svg?branch=develop&service=github :target: https://coveralls.io/github/wooyek/django-pascal-templates?branch=develop


Replace your usual generic view imports with:

.. code:: python

   from pascal_templates.views import DetailView, CreateView, UpdateView, DeleteView, ListView

And in result get additional template_names allowing you to keep templates in folders named after your models:

.. code:: python

   names = [
      'some_app/somemodel_detail.html',
      'some_app/SomeModel/detail.html',   # This is what you get
    ]
