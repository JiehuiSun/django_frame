#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-05-29 13:35:27
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: test_views.py

from django.shortcuts import HttpResponse
from framework.qa_view import PostRPCView
#  from rest_framework.views import APIView
from django.views.generic import View
# from django.views.decorators.http import require_http_methods
#  from rest_framework.generics import
# from rest_framework.decorators import action


def test(req):
    """
    test api
    """
    return HttpResponse("client test success")

class TestParams(PostRPCView):

    decorators = []

    params_dict = {
        "user_id": "required int",
    }

    def post(self, params):
        print("*" * 40)
        print(params)
        return HttpResponse("ok")

