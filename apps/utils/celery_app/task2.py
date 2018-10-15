#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : task2.py
# @Author: 韩朝彪
# @Date  : 2018/10/15
# @Desc  :
import time
from celery_app import app


@app.task
def multiply(x, y):
    time.sleep(10)
    return x * y
