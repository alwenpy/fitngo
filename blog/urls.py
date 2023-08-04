from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.sitemaps.views import sitemap   
from .sitemaps import BlogSitemap

sitemaps={
    "blogs":BlogSitemap
}

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:id>/', views.SingleBlogView.as_view(), name='single_blog'),
    path('test/', views.test, name='test'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
