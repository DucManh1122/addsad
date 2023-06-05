from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import ProductSerializer
from .models import product_details

# Create your views here.
@api_view(['GET'])
def get_product_data(request):
    data = product_details.objects.all()
    if data:
        serializer = ProductSerializer(data,many = True)
        return Response({"status":"Success","data":serializer.data},status=status.HTTP_200_OK)
    return Response({"status":"Failed","message":"Data is not available."},status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def add_product_data(request):
    data ={
            'product_id' : request.data.get('Product Id'),
            'product_category': request.data.get('Product category'),
            'product_name' : request.data.get('Product Name'),
            'availability': request.data.get('Avalability'),
            'price': request.data.get('Price'),
        }
    serializer = ProductSerializer(data=data)
    if serializer.validate(data):
        if serializer.is_valid():
            serializer.create(data)
            return Response({"status":"Success","message":"Product is added Successfully.","data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_category(request):
    lst = [pro.product_category for pro in product_details.objects.all()]
    lst = set(lst)
    print(lst)
    return Response({'data':lst})
    
            
