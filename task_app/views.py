from django.shortcuts import render
from .models import *

# Create your views here.


def home_page_render(request):
    task = Task.objects.all()
    status = Status.objects.all()
    contex = {"tasks" : task, "status" : status }
    return (render(request,'task.html',contex))

def view_details(request,id):
    task = Task.objects.get(pk = id)
    contex = {'task' : task }
    return (render(request,'details.html', contex))

def list_view(request):
    return (render(request,'task_list.html'))