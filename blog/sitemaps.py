from django.contrib.sitemaps import Sitemap
from .models import Blog
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq="weekly"
    priority=0.9
    
    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('single_blog', args=[obj.id])