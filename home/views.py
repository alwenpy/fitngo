from django.shortcuts import render
from blog.models import *
from django.views.decorators.cache import cache_page

@cache_page(60 * 1)
def index(request):
    posts=Blog.objects.all()
    context={"posts":posts}
    return render(request,'index-4.html',context)

@cache_page(60 * 1)
def appointment(request):
    return render(request,'appointment.html')