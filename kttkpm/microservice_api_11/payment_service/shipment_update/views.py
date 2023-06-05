from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from payment.models import payment_status
import requests
import json

# Create your views here.
def shipment_details_update(uname):
    ship_dict = {}
    ### It is used for getting data from payment info.
    user = payment_status.objects.filter(username = uname)
    for data in user.values():
        data
        ship_dict['Product Id'] = data['product_id']
        ship_dict['Quantity'] = data['quantity']
        ship_dict['Payment Status'] = data['status']
        ship_dict['Transaction Id'] = data['id']
        ship_dict['Mobile Number'] = data['mobile']
        ### It is used for getting the user info.
        url = 'http://127.0.0.1:8000/userinfo/'
        d1 = {}
        d1["Email Id"] = uname
        data = json.dumps(d1)
        print(data)
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, data=data, headers=headers)
        val1 = json.loads(response.content.decode('utf-8'))
        print(val1)
        ship_dict['First Name'] = val1['data'][0]['fname']
        ship_dict['Last Name'] = val1['data'][0]['lname']
        ship_dict['Address'] = val1['data'][0]['address']
        ship_dict['Email Id'] = val1['data'][0]['email']
        ### Data is ready for calling the shipment_updates API.
        url = 'http://127.0.0.1:5000/shipment_updates/'
        data = json.dumps(ship_dict)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=data, headers=headers)
        api_resp = json.loads(response.content.decode('utf-8'))
        return api_resp

# @api_view(['GET'])
# def shipment_details_update(request):
#     uname = request.data.get('Email Id')
#     user = payment_status.objects.filter(username = uname)
    
#     headers = {'Content-Type': 'application/json'}
#     url = 'http://127.0.0.1:8000/userinfo/'
#     d1 = {}
#     d1["Email Id"] = uname
#     data = json.dumps(d1)
#     print(data)
#     response = requests.get(url,data=data,headers=headers)
#     val1 = json.loads(response.content.decode('utf-8'))
#     print(val1['data'][0]['fname'])
#     return Response(response.json())