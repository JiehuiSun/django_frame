#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-05-29 13:43:08
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: client/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path(r'test_params', views.TestParams.as_view()),
    path(r'query_user', views.QueryUser.as_view(), name="client_query_user"),
    path(r'list_user', views.ListUser.as_view(), name="client_list_user"),
    path(r'list_problem', views.ListProblem.as_view(), name="client_list_user"),
]
