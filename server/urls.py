#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-05-29 13:46:03
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: server/urls.py

from django.urls import path
from . import views

URL_NAME_PREFIX = "server_"

urlpatterns = [
    path(r'test', views.test),
    path(r'query_user', views.QueryUser.as_view(), name=URL_NAME_PREFIX + "query_user"),
]
