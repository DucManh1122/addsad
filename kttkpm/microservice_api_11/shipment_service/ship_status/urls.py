from django.urls import path
from . import views
urlpatterns = [
    path("shipment_updates/",views.shipment_reg_update),
    path("shipment_status/",views.shipment_status),
]
