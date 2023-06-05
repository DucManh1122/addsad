from django.urls import path
from . import views
urlpatterns = [
    path('getproduct/',views.get_product_data),
    path('addproduct/',views.add_product_data),
    path('getlistcategory/',views.list_category),
]
