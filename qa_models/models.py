#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-05-29 16:21:50
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: models.py

from django.db import models
from client.models import User
from server.models import User as Expert


class Problem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, verbose_name='标题')
    content = models.TextField(null=True, blank=True, default='', verbose_name='内容描述')
    images = models.TextField(null=True, blank=True, default='', verbose_name='相关图片')   # 如果图片跟内容富文本混合则不用改字段
    is_deleted = models.BooleanField(default=False)
    is_activate = models.BooleanField(default=True)
    dt_create = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)
    CHOICES = ((1, "完成"), (2, "进行中"))
    status = models.IntegerField(choices=CHOICES, verbose_name='问题状态', null=True, blank=True)

    def to_dict(self, fields=None, exclude=None):
        data = {}
        for f in self._meta.concrete_fields:
            value = f.value_from_object(self)
            if fields and f.name not in fields:
                continue
            if exclude and f.name in exclude:
                continue
            if isinstance(f, models.DateTimeField):
                value = value.strftime('%Y-%m-%d %H:%M:%S') if value else None
            data[f.name] = value
        return data


class Cost(models.Model):
    """
    费用
    """
    user = models.ForeignKey(Expert, on_delete=models.CASCADE)
    one_month = models.DecimalField(max_digits = 8, decimal_places = 2)
    therr_month = models.DecimalField(max_digits = 8, decimal_places = 2)
    six_month = models.DecimalField(max_digits = 8, decimal_places = 2)
    one_year = models.DecimalField(max_digits = 8, decimal_places = 2)
    dt_create = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)

    def to_dict(self):
        data = {}
        for f in self._meta.concrete_fields:
            value = f.value_from_object(self)
            if isinstance(f, models.DateTimeField):
                value = value.strftime('%Y-%m-%d %H:%M:%S') if value else None
            data[f.name] = value
        return data

class Answer(models.Model):
    """
    """
    user = models.ForeignKey(Expert, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True, default='', verbose_name='解决方案')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    dt_create = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)

    def to_dict(self):
        data = {}
        for f in self._meta.concrete_fields:
            value = f.value_from_object(self)
            if isinstance(f, models.DateTimeField):
                value = value.strftime('%Y-%m-%d %H:%M:%S') if value else None
            data[f.name] = value
        return data


class ProblemTag(models.Model):
    """
    标签(问题)
    """
    tag_name = models.CharField(max_length=32, verbose_name='标签名')
    dt_create = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)


class ProblemLabel(models.Model):
    """
    问题与标签的关联(problem_tag)
    """
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    tag = models.ForeignKey(ProblemTag, on_delete=models.CASCADE)

    class Meta:
        db_table = "qa_models_problem_tag"

