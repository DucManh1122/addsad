from django.urls import path
from . import views
urlpatterns = [
    path("get_payment/",views.add_payment, name='initiate_payment'),
    path("payment_status/",views.user_transaction_info, name='payment_status'),
]
