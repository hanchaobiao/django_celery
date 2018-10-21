#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : celeryconfig.py
# @Author: 韩朝彪
# @Date  : 2018/10/15
# @Desc  :
from datetime import timedelta
from celery.schedules import crontab


# broker设置中间件，backend设置后端存储
BROKER_URL = 'redis://host:6379/1'


BACKEND_URL = 'redis://host:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'  # 时间格式，默认UTC


# 导入指定任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2'
)

CELERY_TIMEZONE = 'Asia/Shanghai'  # 时区

# 定时任务
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'celery_app.task1.add',  # 任务
        'schedule': timedelta(seconds=10),  # 定时时间 每10秒
        'args': (2, 8)  # 参数
    },
    'task2': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=23, minute=33),  # 每天23时29分
        'args': (4, 6)
    }
}

# worker 启动命令  celery -A celery_app worker -l info -P eventlet

# 启动定时任务  celery beat -A celery_app  -l info

# 同时启动beat和worker 不支持windows celery -B -A celery_app -l info
