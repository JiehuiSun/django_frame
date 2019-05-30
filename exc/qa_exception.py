#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# Create: 2019-05-30 09:48:52
# Author: huihui - sunjiehuimail@foxmail.com
# Filename: qa_exception.py

class _QaException(Exception):
    _errcode_dict = {
        0: 'OK',
    }

    def __init__(self, code=0, msg=None, data=None):
        if not self._check_errcode(code):
            raise NotImplementedError(
                'errcode {0} is not implemented'.format(errcode))
        self.errcode = code
        self.errmsg = msg if msg else self._errcode_dict[errcode]
        self.data = data

    def _check_errcode(self, errcode):
        if errcode in self._errcode_dict:
            return True
        return False


class RespOK(_QaException):
    pass


class LogicError(_QaException):
    '''
    LogicError 供API层对外抛出异常使用

    前两位数字按模块功能分类, 后三位数字按异常递增
    '''
    _errcode_dict = {
        10000: '未知逻辑异常',
        10001: '数据异常, 请尝试刷新网页, 或联系系统管理员',

        # 参数
        12001: '请求参数错误',

    }


class SysError(_QaException):
    '''
    SysError 供API层对外抛出异常使用

    前两位数字按模块功能分类, 后三位数字按异常递增
    '''
    _errcode_dict = {
        50000: '未知系统异常',

        # 55 数据库异常
        55001: '数据查询异常',
        55002: '数据创建失败',
        55003: '数据更新失败',
        55004: '数据删除失败'
    }
