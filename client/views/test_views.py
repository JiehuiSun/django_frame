#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-05-29 13:35:27
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: test_views.py

from django.shortcuts import HttpResponse
from framework.qa_view import PostRPCView
from exc.qa_exception import RespOK, LogicError


def test(req):
    """
    test api
    """
    return HttpResponse("client test success")


class TestParams(PostRPCView):
    """
    测试参数的实例
    """

    # decorators = []                       # 理想的装饰器写法

    params_dict = {
        "params1": "required int",          # 参数验证(必填并且为整数)
        "params1": "optional pass",         # 参数验证(可选并不验证value)
    }

    @PostRPCView.compose()                  # 所有装饰器写这里(后期封装成直接一个list属性,类似decorators)
    def post(self, params):
        params1 = params["params1"]

        ret = {
            "code": 0,                      # code 默认为 0 代表成功
            "msg": "OK",                    # msg 默认为 "OK" 代表成功
            "data": {"params1": params1}    # ret data
        }
        return RespOK(**ret)

