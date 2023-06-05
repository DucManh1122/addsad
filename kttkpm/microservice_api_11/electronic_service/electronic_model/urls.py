from django.urls import path
from . import views
urlpatterns = [
    path("list/",views.electronic_list),
    path("add/",views.add_electronic),
    path("get_one/",views.get_by_id),
]
