#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : __init__.py
# @Author: 韩朝彪
# @Date  : 2018/10/15
# @Desc  :
from celery import Celery

app = Celery('demo')

# 通过celery实例加载配置模块

app.config_from_object('celery_app.celeryconfig')

