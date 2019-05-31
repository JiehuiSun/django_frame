#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-05-29 16:55:29
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: user_views.py

from framework.qa_view import GetView
from exc.qa_exception import RespOK, LogicError
from server.backend.api_user import query_user


class QueryUser(GetView):
    """
    """
    params_dict = {
        "user_id": "required"
    }
    def get(self, params):
        user_id = params["user_id"]
        user_dict = query_user(user_id)

        ret_data = {
            "user_info": user_dict
        }
        ret = {
            "data": ret_data
        }
        return RespOK(**ret)
