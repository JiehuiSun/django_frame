#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-05-29 16:21:50
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: models.py

from django.db import models
from client.models import User


class Problem(models.Model):
    title = models.CharField(max_length=128, verbose_name='标题')
    content = models.TextField(null=True, blank=True, default='', verbose_name='内容描述')
    images = models.TextField(null=True, blank=True, default='', verbose_name='相关图片')
    is_deleted = models.BooleanField(default=False)
    is_activate = models.BooleanField(default=True)
    dt_create = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)
    CHOICES = ((1, "完成"), (2, "进行中"))
    status = models.IntegerField(choices=CHOICES, verbose_name='问题状态', null=True, blank=True)

    def to_dict(self, fields=None, exclude=None):
        data = {}
        for f in self._meta.concrete_fields + self._meta.many_to_many:
            value = f.value_from_object(self)
            if fields and f.name not in fields:
                continue
            if exclude and f.name in exclude:
                continue
            if isinstance(f, models.ManyToManyField):
                value = [ i.id for i in value ] if self.pk else None
            if isinstance(f, models.DateTimeField):
                value = value.strftime('%Y-%m-%d %H:%M:%S') if value else None
            data[f.name] = value
        return data
