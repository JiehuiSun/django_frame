#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-05-31 15:47:32
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: problem_views.py


from framework.qa_view import PostView, GetView
from exc.qa_exception import RespOK, LogicError
from qa_backend.api_problem import list_problem_by_id, list_problem_tag


class ListProblem(GetView):
    """
    """
    params_dict = {
        "page_num": "optional",
        "page_size": "optional",
    }

    def get(self, req):

        problem_list = list_problem_by_id()
        ret_data = {
            "problem_list": problem_list
        }
        ret = {
            "data": ret_data
        }
        return RespOK(**ret)


class ListProblemTag(GetView):
    """
    """
    params_dict = {
    }

    def get(self, req):

        tag_list = list_problem_tag()
        ret_data = {
            "tag_list": tag_list
        }
        ret = {
            "data": ret_data
        }
        return RespOK(**ret)
