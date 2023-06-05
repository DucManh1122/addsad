from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields=('id_user','id_product','category_product','name_product','amount_product','description_product','price_product')
    def validate(self, attrs): 
        if not (attrs['id_user'] and attrs['id_product'] and attrs['category_product']):
            raise serializers.ValidationError({"status":"failed","message":"Vui lòng nhập đầy đủ thông tin"})
        return attrs
    def create(self, validated_data):
        cart = Cart.objects.create(
            id_user = validated_data['id_user'],
            id_product = validated_data['id_product'],
            category_product = validated_data['category_product'],
            name_product = validated_data['name_product'],
            amount_product = int(validated_data['amount_product']),
            description_product = validated_data['description_product'],
            price_product = float(validated_data['price_product']),
        )
        cart.save()
        return cart
    