
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart
from .serializer import CartSerializer
import requests
import json

# Create your views here.
@api_view(['GET'])
def get_cart_by_id(request):
    id = request.query_params.get('id_cart')
    try:
        cart = Cart.objects.get(id=id)
        serializer = CartSerializer(cart)
        return Response({"status": "success","data": serializer.data}, status=status.HTTP_200_OK)
    except:
        return Response({"status":"failed","message":"Không tìm thấy danh mục"})
@api_view(['GET'])
def cart_list(request):
    
    id = request.query_params.get('id_user')
    cart = Cart.objects.filter(id_user=id)
    if cart:
        serializer = CartSerializer(cart,many=True)
        return Response({"status": "success","data": serializer.data}, status=status.HTTP_200_OK)
    return Response({"status":"failed","message":"Chưa có sản phẩm trong giỏ hàng"})

@api_view(['POST'])
def delete_pro_from_cart(request):
    data = {
        'id_cart' : request.data.get('Cart Id'),
    }
    try:
        obj = Cart.objects.get(id=data['id_cart'])
        obj.delete()
        return Response({"status":"success","message":"Xóa thành công"}, status=status.HTTP_200_OK)
    except:
        return Response({"status":"failed","message":"Không tìm thấy sản phẩm trong giỏ hàng"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def add_to_cart(request):
    id_product = request.data.get('Product Id')
    category_product = request.data.get('Product Category')
    id_user = request.data.get('User Id')
    pro_data = product_data(id_product,category_product)
    # kiểm tra sản phẩm có tồn tại không
    try:
        pro_data = pro_data['data']
    except:
        return Response({"status":"failed","message":"Không tìm thấy sản phẩm để thêm vào giỏ hàng"}, status=status.HTTP_400_BAD_REQUEST)
    # Kiểm tra sản phẩm đã thêm vào giỏ hàng chưa
    try:
        Cart.objects.get(id_user=id_user, id_product =id_product, category_product = category_product)
        return Response({"status":"failed","message":"Sản phẩm đã được thêm vào giỏ hàng rồi"},status=status.HTTP_400_BAD_REQUEST)
    except:
        data = {
            'id_user' : id_user,
            'id_product' : id_product,
            'category_product' : category_product,
            'name_product': pro_data['name'],
            'amount_product': pro_data['amount'],
            'description_product': pro_data['description'],
            'price_product': pro_data['price'],
        }
        
        serializer = CartSerializer(data=data)
        if serializer.validate(data):
            if serializer.is_valid():
                serializer.create(data)
                return Response({"status":"Success","message":"product is added Successfully.","data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def product_data(productId, productCategory):
    d1={"id_pro":productId}
    # data = json.dumps(d1)
    headers = {'Content-Type': 'application/json'}
    if productCategory == 'Book':
        url = 'http://127.0.0.1:5123/get_one/'
    elif productCategory == 'Shoe':
        url = 'http://127.0.0.1:5124/get_one/'
    elif productCategory == 'Electronic':
        url = 'http://127.0.0.1:5125/get_one/'
    elif productCategory == 'Clothe':
        url = 'http://127.0.0.1:5126/get_one/'
    response = requests.get(url, params=d1, headers=headers)
    val1 = json.loads(response.content.decode('utf-8'))
    return val1