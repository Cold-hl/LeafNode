# _*_ coding:utf-8 _*_
# 开发团队：
# 开发人员：胡子涵
# 开发时间：2022/1/28 10:51
# 文件名称：urls.py
# 开发工具：PyCharm
from django.urls import path
from apps.Test.views import Test

urlpatterns = [
    path('', Test.as_view(), name="test1"),
]
