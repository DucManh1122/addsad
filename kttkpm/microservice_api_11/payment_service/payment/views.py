from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import payment_status
from .serializer import PaymentSerializer
from shipment_update.views import shipment_details_update

# Create your views here.
@api_view(['POST'])
def add_payment(request):
    data ={
        'username' : request.data.get('User Name'),
        'product_id' : request.data.get('Product id'),
        'price' : request.data.get('Product price'),
        'quantity' : request.data.get('Product quantity'),
        'mode_of_payment' : request.data.get('Payment mode'),
        'mobile': request.data.get('Mobile'),
        'status' : 'Success',
    }
    print(data['username'])
    serializer = PaymentSerializer(data=data)
    if serializer.validate(data):
        if serializer.is_valid():
            respdata2 = shipment_details_update(uname= data['username'])
            serializer.create(data)
            return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def user_transaction_info(request):
    username = request.data.get('User Name')
    if not username:
            return Response({"status":"Failed","message":"Fields is mandatory."},status=status.HTTP_400_BAD_REQUEST) 
    else:
        data = payment_status.objects.filter(username=username)
        if not data:
            return Response({"status":"Failed","message":"User Not Found."},status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = PaymentSerializer(data,many = True)
            return Response({"status":"Success","data":serializer.data},status=status.HTTP_200_OK)

    