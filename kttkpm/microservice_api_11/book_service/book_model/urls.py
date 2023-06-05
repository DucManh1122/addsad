from django.urls import path
from . import views
urlpatterns = [
    path("list/",views.book_list),
    path("add/",views.add_book),
    path("get_one/",views.get_by_id)
]
