from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='catalog_home'), 
    path('category/<slug:category_slug>/', views.show_category, name='catalog_category'),
    path('product/<slug:product_slug>/', views.show_product, name='catalog_product'), 
] 