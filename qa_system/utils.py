#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-05-29 17:16:27
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: utils.py

import json
from django.http import HttpResponse


def response_as_json(data, foreign_penetrate=False):
    response = HttpResponse(
        json.dumps(
            data,
            ensure_ascii=False
        ),
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=0, foreign_penetrate=False, **kwargs):
    data = {
        "code": code,
        "msg": "OK",
        "data": data,
    }
    return response_as_json(data, foreign_penetrate=foreign_penetrate)


def json_error(error_string="", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)
