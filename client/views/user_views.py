#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-05-29 16:55:29
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: user_views.py

from framework.qa_view import GetView
from exc.qa_exception import RespOK, LogicError
from client.models import User


class QueryUser(GetView):
    """
    """
    params_dict = {
        "user_id": "required"
    }
    def get(self, params):
        user_id = params["user_id"]
        user_obj = User.objects.filter(pk=user_id).first()
        user_dict = user_obj.to_dict()

        ret_data = {
            "user_info": user_dict
        }
        ret = {
            "data": ret_data
        }
        return RespOK(**ret)


class ListUser(GetView):
    """
    """
    def get(self, req):
        user_obj_list = User.objects.all()
        user_list = [i.to_dict() for i in user_obj_list]
        ret_data = {
            "user_list": user_list
        }
        ret = {
            "data": ret_data
        }
        return RespOK(**ret)
