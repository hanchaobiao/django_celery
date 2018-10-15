#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : app.py
# @Author: 韩朝彪
# @Date  : 2018/10/15
# @Desc  :
from celery_app import task1
from celery_app import task2


task1.add.delay(4, 6)
task2.multiply.delay(2, 10)

print('end.........')


# from tasks import add
#
# """
# 消费：
#     celery -A tasks worker -l INFO
#     celery -A tasks worker -l info -P eventlet  :Python3+celery4.1需使用此启动方式
#     启动一个worker
#     #查询文档，了解到该命令中-A参数表示的是Celery APP的名称，这个实例中指的就是tasks.py（和文件名一致），
#     后面的tasks就是APP的名称，worker是一个执行任务角色，后面的loglevel=info记录日志类型默认是info,
#     这个命令启动了一个worker,用来执行程序中add这个加法任务（task）
# """
#
#
# if __name__ == '__main__':
#     print('start task....')
#     result = add.delay(2, 8)  # 提交任务，将任务提交到中间件
#     print(result.ready())  # 是否计算结束
#     print(result.get())  # 取回返回结果
#     print('end func....')
#     print(result)
