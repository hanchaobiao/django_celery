from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from course.tasks import CourseTask


def do(request):
    # 执行异步任务
    print('start do request')
    # CourseTask.delay()
    CourseTask.apply_async(args=('hello', ), queue='work_queue')  # 指定queue
    print('end do request')
    return JsonResponse({'result': 'ok'})
