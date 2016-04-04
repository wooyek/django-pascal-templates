# coding=utf-8
# Copyright 2015 Brave Labs sp. z o.o.
# All rights reserved.
#
# This source code and all resulting intermediate files are CONFIDENTIAL and
# PROPRIETY TRADE SECRETS of Brave Labs sp. z o.o.
# Use is subject to license terms. See NOTICE file of this project for details.
from django.db import models
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.list import MultipleObjectTemplateResponseMixin
from django.views import generic


class TemplatePathMixin(object):
    template_name_path_pattern = "{app_label}/{object_name}/{template_name_suffix}.html"

    def get_template_path(self, meta=None, **kwargs):
        kwargs.setdefault('template_name_suffix', self.get_template_name_suffix())
        return self.template_name_path_pattern.format(**kwargs)

    def get_template_name_suffix(self):
        if self.template_name_suffix.startswith("_"):
            return self.template_name_suffix[1:]
        return self.template_name_suffix


class SinglePascalCaseTemplateMixin(TemplatePathMixin, SingleObjectTemplateResponseMixin):
    def get_template_names(self):
        names = super(SinglePascalCaseTemplateMixin, self).get_template_names()
        if isinstance(self.object, models.Model):
            meta = self.object._meta
            if self.object._deferred:
                meta = self.object._meta.proxy_for_model._meta
            template_path = self.get_template_path(meta, app_label=meta.app_label, object_name=meta.object_name)
            names.append(template_path)
        elif hasattr(self, 'model') and self.model is not None and issubclass(self.model, models.Model):
            meta = self.model._meta
            template_path = self.get_template_path(meta, app_label=meta.app_label, object_name=meta.object_name)
            names.append(template_path)
        return names


class MultiplePascalCaseTemplateMixin(TemplatePathMixin, MultipleObjectTemplateResponseMixin):
    def get_template_names(self):
        names = super(MultiplePascalCaseTemplateMixin, self).get_template_names()
        if hasattr(self.object_list, 'model'):
            meta = self.object_list.model._meta
            template_path = self.get_template_path(meta, app_label=meta.app_label, object_name=meta.object_name)
            names.append(template_path)
        return names


class DetailView(generic.DetailView, SinglePascalCaseTemplateMixin):
    __doc__ = generic.DetailView.__doc__


class DateDetailView(generic.DateDetailView, SinglePascalCaseTemplateMixin):
    __doc__ = generic.DateDetailView.__doc__


class CreateView(generic.CreateView, SinglePascalCaseTemplateMixin):
    __doc__ = generic.CreateView.__doc__


class DeleteView(generic.DeleteView, SinglePascalCaseTemplateMixin):
    __doc__ = generic.DeleteView.__doc__


class UpdateView(generic.UpdateView, SinglePascalCaseTemplateMixin):
    __doc__ = generic.UpdateView.__doc__


class ArchiveIndexView(generic.ArchiveIndexView, MultiplePascalCaseTemplateMixin):
    __doc__ = generic.ArchiveIndexView.__doc__


class DayArchiveView(generic.DayArchiveView, MultiplePascalCaseTemplateMixin):
    __doc__ = generic.DayArchiveView.__doc__


class MonthArchiveView(generic.MonthArchiveView, MultiplePascalCaseTemplateMixin):
    __doc__ = generic.MonthArchiveView.__doc__


class TodayArchiveView(generic.TodayArchiveView, MultiplePascalCaseTemplateMixin):
    __doc__ = generic.TodayArchiveView.__doc__


class WeekArchiveView(generic.WeekArchiveView, MultiplePascalCaseTemplateMixin):
    __doc__ = generic.WeekArchiveView.__doc__


class YearArchiveView(generic.YearArchiveView, MultiplePascalCaseTemplateMixin):
    __doc__ = generic.YearArchiveView.__doc__


class ListView(generic.ListView, MultiplePascalCaseTemplateMixin):
    __doc__ = generic.ListView.__doc__
