from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

import time
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

# 实例化调度器
scheduler = BackgroundScheduler(timezone='Asia/Shanghai')
# 调度器使用DjangoJobStore()
scheduler.add_jobstore(DjangoJobStore(), "default")


# 设置定时任务，选择方式为interval，时间间隔为10s
# 另一种方式为每天固定时间执行任务，对应代码为：
# @register_job(scheduler, 'cron', day_of_week='mon-fri', hour='9', minute='30', second='10',id='task_time', replace_existing=True)
# 时间间隔3秒钟打印一次当前的工作状态
# 使用replace_existing标志告诉它替换现有作业
@register_job(scheduler, "interval", seconds=10, id='test_job', replace_existing=True)
def test_job():
    # 工作代码
    # print(第一次)
    while True:
        print("test_job:正在工作")
        time.sleep(1)


def test(request):
    if request.method == "POST":
        state = 1
        start = request.POST.get('start', "")
        over = request.POST.get('over', "")
        if start:
            # 注册定时任务（已过时）
            # register_events(scheduler)
            # 开始定时任务
            scheduler.resume_job("test_job")
            state = 1
            print("test_job:开始工作")
        if over:
            # 停止定时器
            state = 0
            print("test_job:工作结束")
            scheduler.pause_job("test_job")

    else:
        scheduler.start()

    return render(request, 'Node.html', locals())
