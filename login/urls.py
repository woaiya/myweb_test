#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from login import views


app_name = 'login'
urlpatterns = [
    path(r'index/', views.index, name='index'),
    path(r'login_ajax', views.ajax_login, name='login_ajax'),
]