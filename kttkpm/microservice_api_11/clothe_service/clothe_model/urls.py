from django.urls import path
from . import views
urlpatterns = [
    path("list/",views.clothe_list),
    path("add/",views.add_clothe),
    path("get_one/",views.get_by_id),
]
