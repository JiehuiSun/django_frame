#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-05-29 16:55:29
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: user_views.py

from django.shortcuts import HttpResponse
from django.views.generic import View
from qa_system.utils import json_response, json_error
from client.models import User
from qa_models.models import Problem


class QueryUser(View):
    """
    """
    def get(self, req):
        user_id = req.GET.get("user_id")
        user_obj = User.objects.filter(pk=user_id).first()
        user_dict = user_obj.to_dict()

        ret = {
            "user_info": user_dict
        }
        return json_response(ret)


class ListUser(View):
    """
    """
    def get(self, req):
        user_obj_list = User.objects.all()
        user_list = [i.to_dict() for i in user_obj_list]
        ret = {
            "user_list": user_list
        }
        return json_response(ret)



class ListProblem(View):
    """
    """
    def get(self, req):
        problem_obj_list = Problem.objects.all()
        problem_list = [i.to_dict() for i in problem_obj_list]
        ret = {
            "problem_list": problem_list
        }
        return json_response(ret)
