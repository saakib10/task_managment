from django.shortcuts import render
from .models import *

# Create your views here.


def home_page_render(request):
    task = Task.objects.all()
    status = Status.objects.all()
    contex = {"tasks" : task, "status" : status }
    return (render(request,'task.html',contex))

def details(request):
    return (render(request,'details.html'))