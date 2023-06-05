from django.urls import path
from . import views
urlpatterns = [
    path("shipment_updates/",views.shipment_details_update, name="shipment_updates"),
]
