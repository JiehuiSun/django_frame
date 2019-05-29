#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-05-29 13:38:13
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: test_views.py

from django.shortcuts import render, HttpResponse


def test(req):
    """
    test api
    """
    return HttpResponse("client test success")
