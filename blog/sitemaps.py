from django.contrib.sitemaps import GenericSitemap
from .models import Blog

blog_info_dict = {
    'queryset': Blog.objects.all(),
    'date_field': 'created_at',
}
sitemaps = {
    'blog': GenericSitemap(blog_info_dict),
}