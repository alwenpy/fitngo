from django.shortcuts import render
from django.views.generic import View
from .models import Blog
from django.shortcuts import get_object_or_404


class HomeView(View):
    def get(self, request, *args, **kwargs):
        post = Blog.objects.all().order_by('catagories', '-created_at')
        context = {
            'post': post,
        }
        return render(request, 'blog.html', context)
    


class SingleBlogView(View):
    def get(self,request,id,*args,**kwargs):
        post = get_object_or_404(Blog, id=id)
        context = {
            'post': post,
        }
        return render(request, 'single_blog.html', context)