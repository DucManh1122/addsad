
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Clothe
from .serializer import ClotheSerializer,ClotheSerializer1

# Create your views here.
@api_view(['GET'])
def clothe_list(request):
    clothes = Clothe.objects.all()
    if clothes:
        serializer = ClotheSerializer1(clothes,many=True)
        return Response({"status": "success","data": serializer.data}, status=status.HTTP_200_OK)
    return Response({"status":"failed","message":"Danh mục sẽ được cập nhật sớm nhất có thể"})

@api_view(['GET'])
def get_by_id(request):
    id = request.query_params.get('id_pro')
    try:
        clothe = Clothe.objects.get(id=id)
        serializer = ClotheSerializer(clothe)
        print(serializer.data)
        return Response({"status": "success","data": serializer.data}, status=status.HTTP_200_OK)
    except:
        return Response({"status":"failed","message":"Không tìm thấy Clothe"})

@api_view(['POST'])
def add_clothe(request):
    data = {
        'name' : request.data.get('Name'),
        'made_in' : request.data.get('Info'),
        'amount' : request.data.get('Amount'),
        'description' : request.data.get('Description'),
        'price' : request.data.get('Price'),
        'category' : 'Clothe',
    }
    serializer = ClotheSerializer(data=data)
    if serializer.validate(data):
        if serializer.is_valid():
            serializer.create(data)
            return Response({"status":"Success","message":"Clothe is added Successfully.","data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    