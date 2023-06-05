from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_model.models import user_registration
from .serializer import UserInfoSerializer

# Create your views here.
@api_view(['GET','POST'])
def user_info(request):
    username = request.data.get('Email Id')
    data = user_registration.objects.filter(email = username)
    print(data)
    if data:
        serializer = UserInfoSerializer(data,many=True)
        return Response({"status":"Success","data":serializer.data},status=status.HTTP_200_OK)
    else:
        return Response({"status":"Failed","message":"User Not Found."},status=status.HTTP_400_BAD_REQUEST)