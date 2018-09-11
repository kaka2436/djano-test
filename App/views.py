from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def add_user(request):
    user = Users()
    user.name = '李四'
    user.age = 30
    user.sex = True
    user.birth = '2009-02-02 09:08:12'
    user.save()
    return HttpResponse('<h1>添加成功</h1>')