#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-05-29 13:43:08
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: client/urls.py

from django.urls import path
from . import test_views

urlpatterns = [
    path(r'test', test_views.test),
]
