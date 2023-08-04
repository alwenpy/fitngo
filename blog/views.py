from django.shortcuts import render
from django.views.generic import View
from .models import Blog
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


class HomeView(View):
    def get(self, request, *args, **kwargs):
        posts = Blog.objects.all().order_by('catagories', '-created_at')
        paginator = Paginator(posts, 1)  # Pass the queryset 'posts' to Paginator
        page_number = request.GET.get('page')
        data = paginator.get_page(page_number)
        context = {
            'posts': data, 
        }
        return render(request, 'blog.html', context)
    


class SingleBlogView(View):
    def get(self,request,id,*args,**kwargs):
        post = get_object_or_404(Blog, id=id)
        context = {
            'post': post,
        }
        return render(request, 'single_blog.html', context)
    
    

def test(request):
    post=Blog.objects.all()     
    context = { 'post': post, }
    return render(request,'blog_test.html',context)
