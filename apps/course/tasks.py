#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : task.py
# @Author: 韩朝彪
# @Date  : 2018/10/15
# @Desc  :
import time
from celery.task import Task


class CourseTask(Task):

    # 指定任务名
    name = 'course-task'

    def run(self, *args, **kwargs):
        print('start course task')
        time.sleep(4)
        print('args={}, kwargs={}'.format(args, kwargs))
        print('end course task')
