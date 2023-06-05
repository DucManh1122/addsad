from django.shortcuts import render
from .serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def user_login(request):
    if request.method == 'POST':
        data = {
            'email': request.data.get('Email Id'),
            'password': request.data.get('Password')
        }
        serializer = LoginSerializer(data=data)
        if serializer.validate(data):
            return Response({"status":"Success","message":"Welcome to Ecommerce website......"},status=status.HTTP_200_OK) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        


# from rest_framework import viewsets
# from user_model.models import user_registration

# from .serializers import LoginSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = user_registration.objects.all()
#     serializer_class = LoginSerializer