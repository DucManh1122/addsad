from django.urls import path, re_path
from django.views.static import serve
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('catalog/', views.home),
    # re_path(r'^static/(?P<path>.*)$', serve, { 'document_root' : '/static' }), 
]