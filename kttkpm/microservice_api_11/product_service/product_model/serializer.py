from rest_framework import serializers
from .models import product_details

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_details
        fields = ('product_id','product_category','product_name','availability','price')
    def validate(self, attrs):
        if not (attrs['product_id'] and attrs['product_category'] and attrs['product_name'] and attrs['availability'] and attrs['price']):
            raise serializers.ValidationError({"status":"Failed","message":"All fields are mandatory."})
        else:
            try:
                product_details.objects.get(product_id = attrs['product_id'])
            except product_details.DoesNotExist:
                return attrs
            else:
                raise serializers.ValidationError({"status":"Failed","message":"ID khong duoc phep trung"})
    def create(self, validated_data):
        product = product_details.objects.create(
            product_id = validated_data['product_id'],
            product_category = validated_data['product_category'],
            product_name = validated_data['product_name'],
            availability =  validated_data['availability'],
            price = validated_data['price'],
        )
        product.save()
        return product
        