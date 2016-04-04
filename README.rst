django-pascal-templates
=======================

Django generic views with PascalCase template paths with model named folders.

Replace your usual generic view imports with:

.. code:: python

   from pascal_templates.views import DetailView, CreateView, UpdateView, DeleteView, ListView

And in result get additional template_names allowing you to keep templates in folders named after your models:

.. code:: python

   names = [
      'some_app/somemodel_detail.html',
      'some_app/SomeModel/detail.html',   # This is what you get
    ]
