#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-05-31 17:53:04
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: api_user.py


from client.models import User


def query_user(user_id):
    """
    """
    user_obj = User.objects.filter(pk=user_id).first()
    user_dict = user_obj.to_dict()

    return user_dict


def list_user(user_ids):
    """
    """
    pass
