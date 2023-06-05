from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializer import OrderSerializer
import requests
import json

@api_view(['GET'])
def order_list(request):
    
    username = request.query_params.get('name_user')
    orders = Order.objects.filter(name_user=username)
    if orders:
        serializer = OrderSerializer(orders,many=True)
        return Response({"status": "success","data": serializer.data}, status=status.HTTP_200_OK)
    return Response({"status":"failed","message":"Chưa đặt hàng sản phẩm nào"})

@api_view(['POST'])
def add_order(request):
    id_cart = request.data.get('Cart Id')
    name_user = request.data.get('Username')
    u_data = user_data(name_user)
    c_data = cart_data(id_cart)
    # kiểm tra sản phẩm có tồn tại không
    try:
        u_data = u_data['data'][0]
    except:
        return Response({"status":"failed","message":"Không tìm thấy user"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        c_data = c_data['data']
    except:
        return Response({"status":"failed","message":"Không tìm thấy cart item"}, status=status.HTTP_400_BAD_REQUEST)
    data = {
        'name_user' : u_data['email'],
        'address_user' : u_data['address'],
        'mobile_user': u_data['mobile'],
        'id_product': c_data['id_product'],
        'category_product': c_data['category_product'],
        'name_product': c_data['name_product'],
        'amount_product': c_data['amount_product'],
        'description_product': c_data['description_product'],
        'price_product': c_data['price_product'],
    }
        
    serializer = OrderSerializer(data=data)
    if serializer.validate(data):
        if serializer.is_valid():
            serializer.create(data)
            delete_cart_item(id_cart)
            return Response({"status":"Success","message":"Order is added Successfully.","data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def user_data(name_user):
    d1={"Email Id":name_user}
    data = json.dumps(d1)
    headers = {'Content-Type': 'application/json'}
    url = 'http://127.0.0.1:8000/userinfo/'
    response = requests.get(url, data=data, headers=headers)
    val1 = json.loads(response.content.decode('utf-8'))
    return val1
def cart_data(id_cart):
    d1={"id_cart":id_cart}
    # data = json.dumps(d1)
    headers = {'Content-Type': 'application/json'}
    url = 'http://127.0.0.1:5127/get_one/'
    response = requests.get(url, params=d1, headers=headers)
    val1 = json.loads(response.content.decode('utf-8'))
    return val1

def delete_cart_item(id_cart):
    d1={"Cart Id":id_cart}
    data = json.dumps(d1)
    headers = {'Content-Type': 'application/json'}
    url = 'http://127.0.0.1:5127/delete/'
    requests.post(url, data=data, headers=headers)