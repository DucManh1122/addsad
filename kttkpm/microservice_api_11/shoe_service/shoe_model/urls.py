from django.urls import path
from . import views
urlpatterns = [
    path("list/",views.shoe_list),
    path("add/",views.add_shoe),
    path("get_one/",views.get_by_id),
]
