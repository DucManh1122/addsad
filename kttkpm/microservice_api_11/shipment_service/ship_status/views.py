from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import shipment
from .serializer import ShipmentSerializer

# Create your views here.
@api_view(['POST'])
def shipment_reg_update(request):
    data = {
        'fname' : request.data.get("First Name"),
        'lname' : request.data.get("Last Name"),
        'email' : request.data.get("Email Id"),
        'mobile' : request.data.get("Mobile Number"),
        'address' : request.data.get("Address"),
        'product_id' : request.data.get("Product Id"),
        'quantity' : request.data.get("Quantity"),
        'payment_status' : request.data.get("Payment Status"),
        'transaction_id' : request.data.get("Transaction Id"),
        'shipment_status' : "ready to dispatch"
    }
    serializer = ShipmentSerializer(data=data)
    if serializer.validate(data):
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Success","data":serializer.data},status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def shipment_status(request):
    email = request.data.get('Email Id')
    print(email)
    res = shipment.objects.filter(email = email)
    print(res)
    if not res:
        return Response({"status":"Failed","message":"shipment data for user is not available"})
    else:
        serializer = ShipmentSerializer(res,many=True)
        return Response({"status":"Success","data":serializer.data})
    