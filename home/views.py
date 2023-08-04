from django.shortcuts import render
from blog.models import *


def index(request):
    posts=Blog.objects.all()
    context={"posts":posts}
    return render(request,'index-4.html',context)

def appointment(request):
    return render(request,'appointment.html')