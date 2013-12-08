#coding=utf8
from django.shortcuts import render
import time
def index(request):
    return render(request,'index.html',{'time':time.strftime('%Y-%m-%d %H:%M')})
