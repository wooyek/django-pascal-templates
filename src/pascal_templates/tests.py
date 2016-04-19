# coding=utf-8
# Copyright 2016 Janusz Skonieczny

from unittest import TestCase

from pascal_templates.views import SinglePascalCaseTemplateMixin, DetailView, DateDetailView, CreateView, DeleteView, UpdateView, ListView


class TestPascalTemplateMixins(TestCase):
    @classmethod
    def setUpClass(cls):
        import django
        from django.conf import settings
        from django.db import models
        settings.configure()
        django.setup()

        class SomeModel(models.Model):
            class Meta:
                app_label = "some_app"

        class SomeProxyModel(SomeModel):
            class Meta:
                app_label = "some_app"
                proxy = True

        cls.model = SomeModel
        cls.proxy = SomeProxyModel

    def test_template_name_suffix(self):
        mixin = SinglePascalCaseTemplateMixin()
        self.assertEqual("detail", mixin.get_template_name_suffix())

    def test_template_name_suffix2(self):
        mixin = SinglePascalCaseTemplateMixin()
        mixin.template_name_suffix = "custom"
        self.assertEqual("custom", mixin.get_template_name_suffix())

    def test_single_object(self):
        mixin = SinglePascalCaseTemplateMixin()
        path = mixin.get_template_path(a="1", b="b", app_label="app", object_name="SomeModel")
        self.assertEqual("app/SomeModel/detail.html", path)

    def test_model_names(self):
        mixin = SinglePascalCaseTemplateMixin()
        mixin.object = None
        mixin.model = self.model
        names = mixin.get_template_names()
        self.assertEqual(['some_app/somemodel_detail.html', 'some_app/SomeModel/detail.html'], names)

    def test_proxy_model_names(self):
        mixin = SinglePascalCaseTemplateMixin()
        mixin.object = None
        mixin.model = self.proxy
        names = mixin.get_template_names()
        self.assertEqual(['some_app/someproxymodel_detail.html', 'some_app/SomeProxyModel/detail.html'], names)

    def test_object_names(self):
        mixin = SinglePascalCaseTemplateMixin()
        mixin.object = self.model()
        names = mixin.get_template_names()
        self.assertEqual(['some_app/somemodel_detail.html', 'some_app/SomeModel/detail.html'], names)

    def test_proxy_object_names(self):
        mixin = SinglePascalCaseTemplateMixin()
        mixin.object = self.proxy()
        names = mixin.get_template_names()
        self.assertEqual(['some_app/someproxymodel_detail.html', 'some_app/SomeProxyModel/detail.html'], names)

    def test_ListView(self):
        view = ListView()
        view.object_list = self.model.objects.all()
        names = view.get_template_names()
        self.assertEqual(['some_app/somemodel_list.html', 'some_app/SomeModel/list.html'], names)

    def test_DetailView(self):
        view = DetailView()
        view.object = None
        view.model = self.model
        names = view.get_template_names()
        self.assertEqual(['some_app/somemodel_detail.html', 'some_app/SomeModel/detail.html'], names)

    def test_DateDetailView(self):
        view = DateDetailView()
        view.object = None
        view.model = self.model
        names = view.get_template_names()
        self.assertEqual(['some_app/somemodel_detail.html', 'some_app/SomeModel/detail.html'], names)

    def test_CreateView(self):
        view = CreateView()
        view.model = self.model
        view.object = None
        names = view.get_template_names()
        self.assertEqual(['some_app/somemodel_form.html', 'some_app/SomeModel/form.html'], names)

    def test_UpdateView(self):
        view = UpdateView()
        view.object = None
        view.model = self.model
        names = view.get_template_names()
        self.assertEqual(['some_app/somemodel_form.html', 'some_app/SomeModel/form.html'], names)

    def test_DeleteView(self):
        view = DeleteView()
        view.object = None
        view.model = self.model
        names = view.get_template_names()
        self.assertEqual(['some_app/somemodel_confirm_delete.html', 'some_app/SomeModel/confirm_delete.html'], names)

