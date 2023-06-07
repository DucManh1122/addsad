
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializer import BookSerializer,BookSerializer1

# Create your views here.
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    if books:
        serializer = BookSerializer1(books,many=True)
        return Response({"status": "success","data": serializer.data}, status=status.HTTP_200_OK)
    return Response({"status":"failed","message":"Sách sẽ được cập nhật sớm nhất có thể"})

@api_view(['GET'])
def get_by_id(request):
    id = request.query_params.get('id_pro')
    try:
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book)
        print(serializer.data)
        return Response({"status": "success","data": serializer.data}, status=status.HTTP_200_OK)
    except:
        return Response({"status":"failed","message":"Không tìm thấy sách"})

@api_view(['POST'])
def add_book(request):
    data = {
        'name' : request.data.get('Name'),
        'author' : request.data.get('Info'),
        'amount' : request.data.get('Amount'),
        'description' : request.data.get('Description'),
        'price' : request.data.get('Price'),
        'category' : "Book",
    }
    serializer = BookSerializer(data=data)
    if serializer.validate(data):
        if serializer.is_valid():
            serializer.create(data)
            return Response({"status":"Success","message":"Book is added Successfully.","data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    