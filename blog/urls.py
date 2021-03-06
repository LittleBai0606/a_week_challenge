#!/usr/bin/env python
# encoding: utf-8

"""
@author: littlewhite
@license: MIT Licence
@contact: littlewhite0606@qq.com
@site: https://littlebai0606.github.io/
@software: PyCharm
@file: urls.py
@time: 2018/3/1 上午11:08
"""

from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<blog_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
]

