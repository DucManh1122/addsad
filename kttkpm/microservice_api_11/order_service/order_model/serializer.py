from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields=('name_user','address_user','mobile_user','id_product','category_product','name_product','amount_product','description_product','price_product')
    def create(self, validated_data):
        order = Order.objects.create(
            id_product = validated_data['id_product'],
            category_product = validated_data['category_product'],
            name_product = validated_data['name_product'],
            amount_product = int(validated_data['amount_product']),
            description_product = validated_data['description_product'],
            price_product = float(validated_data['price_product']),
            name_user = validated_data['name_user'],
            address_user = validated_data['address_user'],
            mobile_user = validated_data['mobile_user'],
        )
        order.save()
        return order
    