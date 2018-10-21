#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : celeryconfig.py
# @Author: 韩朝彪
# @Date  : 2018/10/15
# @Desc  : celery配置文件
from datetime import timedelta
import djcelery
from celery import platforms


djcelery.setup_loader()


platforms.C_FORCE_ROOT = True  # 达P蠾L以root潔¨彈·达P蠾L


CELERY_QUEUES = {
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks'
    },
    'work_queue': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks'
    }
}


# 指定worker队列，将定时队列与worker队列区分开，防止影响
CELERY_DEFAULT_QUEUE = 'work_queue'

# 导入任务模块
CELERY_IMPORTS = (
    'apps.course.tasks'
)


# 有些情况下可以防止死锁

CELERYD_FORCE_EXECV = True


# 设置并发worker数
CELERYD_CONCURRENCY = 4

# 允许重试次数

CELERY_ACKS_LATE = True

# 每个worker最多执行100个任务被销毁，防止内存泄漏

CELERY_MAX_TASKS_PER_CHILD = 100

# 单个任务最大运行时间

CELERYD_TASK_TIME_LIMIT = 12*30


# 定时任务
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'course-task',  # 任务
        'schedule': timedelta(seconds=10),  # 定时时间 每10秒
        'args': (2, 8),  # 参数
        'options': {
            'queue': 'beat_tasks'
        }
    },

}
