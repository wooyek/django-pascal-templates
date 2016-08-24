# coding=utf-8
# Copyright 2016 Janusz Skonieczny.

from django.db import models
from django.views import generic
from django.views.generic import list
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.list import MultipleObjectTemplateResponseMixin


class TemplatePathMixin(object):
    template_name_path_pattern = "{app_label}/{object_name}/{template_name_suffix}.html"

    def get_template_path(self, meta=None, **kwargs):
        """
        Formats template_name_path_pattern with kwargs given.
        """
        if 'template_name_suffix' not in kwargs or kwargs.get('template_name_suffix') is None:
            kwargs['template_name_suffix'] = self.get_template_name_suffix()
        return self.template_name_path_pattern.format(**kwargs)

    def get_template_name_suffix(self):
        """
        Removes an underscore from default template_name_suffix and returns it
        """
        if self.template_name_suffix.startswith("_"):
            return self.template_name_suffix[1:]
        return self.template_name_suffix


class SinglePascalCaseTemplateMixin(TemplatePathMixin, SingleObjectTemplateResponseMixin):
    def get_template_names(self):
        names = super(SinglePascalCaseTemplateMixin, self).get_template_names()
        name = self.get_template_name()
        if name:
            names.append(name)
        return names

    def get_template_name(self, template_name_suffix=None):
        """
        Generates a template path name based on model and app.
        :param template_name_suffix: pass a custom suffix or leave empty for default
        :return: template path
        """
        if isinstance(self.object, models.Model):
            meta = self.object._meta
            return self.get_template_path(meta, app_label=meta.app_label, object_name=meta.object_name, template_name_suffix=template_name_suffix)
        elif hasattr(self, 'model') and self.model is not None and issubclass(self.model, models.Model):
            meta = self.model._meta
            return self.get_template_path(meta, app_label=meta.app_label, object_name=meta.object_name, template_name_suffix=template_name_suffix)


class MultiplePascalCaseTemplateMixin(TemplatePathMixin, MultipleObjectTemplateResponseMixin):
    def get_template_names(self):
        names = super(MultiplePascalCaseTemplateMixin, self).get_template_names()
        name = self.get_template_name()
        if name:
            names.append(name)
        return names

    def get_template_name(self, template_name_suffix=None):
        """
        Generates a template path name based on model and app.
        :param template_name_suffix: pass a custom suffix or leave empty for default
        :return: template path
        """
        if hasattr(self.object_list, 'model'):
            meta = self.object_list.model._meta
            return self.get_template_path(meta, app_label=meta.app_label, object_name=meta.object_name, template_name_suffix=template_name_suffix)


class DetailView(SinglePascalCaseTemplateMixin, generic.DetailView):
    __doc__ = generic.DetailView.__doc__


class DateDetailView(SinglePascalCaseTemplateMixin, generic.DateDetailView):
    __doc__ = generic.DateDetailView.__doc__


class CreateView(SinglePascalCaseTemplateMixin, generic.CreateView):
    # __doc__ = generic.CreateView.__doc__
    pass


class DeleteView(SinglePascalCaseTemplateMixin, generic.DeleteView):
    __doc__ = generic.DeleteView.__doc__


class UpdateView(SinglePascalCaseTemplateMixin, generic.UpdateView):
    __doc__ = generic.UpdateView.__doc__


class ArchiveIndexView(MultiplePascalCaseTemplateMixin, generic.ArchiveIndexView):
    __doc__ = generic.ArchiveIndexView.__doc__


class DayArchiveView(MultiplePascalCaseTemplateMixin, generic.DayArchiveView):
    __doc__ = generic.DayArchiveView.__doc__


class MonthArchiveView(MultiplePascalCaseTemplateMixin, generic.MonthArchiveView):
    __doc__ = generic.MonthArchiveView.__doc__


class TodayArchiveView(MultiplePascalCaseTemplateMixin, generic.TodayArchiveView):
    __doc__ = generic.TodayArchiveView.__doc__


class WeekArchiveView(MultiplePascalCaseTemplateMixin, generic.WeekArchiveView):
    __doc__ = generic.WeekArchiveView.__doc__


class YearArchiveView(MultiplePascalCaseTemplateMixin, generic.YearArchiveView):
    __doc__ = generic.YearArchiveView.__doc__


class ListView(MultiplePascalCaseTemplateMixin, list.ListView):
    # __doc__ = generic.ListView.__doc__
    pass
