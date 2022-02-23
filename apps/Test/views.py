from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.

class Test(View):
    """

    """

    def get(self, requesst):
        return HttpResponse("demo1")
