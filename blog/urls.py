#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from blog import views


app_name = 'blog'
urlpatterns = [
    path(r'index/', views.index, name='index'),
    path(r'body/<body_id>', views.body, name='body_page'),
    path(r'edit/<body_id>', views.edit, name='edit'),
    path(r'add', views.add, name='add'),
    path(r'delete/<body_id>', views.delete, name='delete'),
]