#! /usr/bin/env python
# -*- coding:utf-8 -*-

import threading


class Thread(threading.Thread):
    """
    自定义线程类
    属性：
    target:传入外部函数，用户线程调用
    args:函数参数
    """

    def __init__(self, target=None, args=(), kwargs=None):
        super(Thread, self).__init__()  # 调用父类的构造函数
        if kwargs is None:
            kwargs = {}
        self._target = target
        self._args = args
        self._kwargs = kwargs

    def run(self):
        """开始运行当前线程"""
        self._target(*self._args, **self._kwargs)

    def get_threading_num(self):
        """获取当前正在运行的线程数量"""
        return len(threading.enumerate())
