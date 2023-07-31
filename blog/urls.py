from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:id>/', views.SingleBlogView.as_view(), name='single_blog'),
    path('test/', views.test, name='test'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
