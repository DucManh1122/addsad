from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home), 
    path('category/<slug:category_slug>/', views.show_category, name='catalog_category'),
    path('product/<slug:product_slug>/', views.show_product, name='catalog_product'), 
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)