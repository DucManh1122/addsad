from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import user_registration
from .serializers import RegisterSerializers


@api_view(['GET', 'POST'])
def Register(request):
    if request.method == 'POST': # user posting data
        data ={
            'fname' : request.data.get('First Name'),
            'lname': request.data.get('Last Name'),
            'email' : request.data.get('Email Id'),
            'mobile': request.data.get('Mobile Number'),
            'password': request.data.get('Password'),
            'confirm_password': request.data.get('Confirm Password'),
            'address': request.data.get('Address')
        }
        serializer = RegisterSerializers(data=data)
        if serializer.validate(data):
            if serializer.is_valid():
            #     print(serializer.data)
                serializer.create(data) # save to db
                return Response({"status":"Success","message":"User is registered Successfully.","data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
