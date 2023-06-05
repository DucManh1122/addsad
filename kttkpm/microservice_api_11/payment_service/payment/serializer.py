from rest_framework import serializers
from .models import  payment_status

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment_status
        fields = ('username','product_id','price','quantity','mode_of_payment','mobile')
    def validate(self, attrs):
        if not(attrs['username'] and attrs['product_id'] and attrs['price'] and attrs['quantity'] and attrs['mode_of_payment'] and attrs['mobile']):
            raise serializers.ValidationError({"status":"Failed","message":"All fields are mandatory."})
        return attrs
    def create(self, validated_data):
        pay = payment_status.objects.create(
            username = validated_data['username'],
            product_id = validated_data['product_id'],
            price = validated_data['price'],
            quantity = validated_data['quantity'],
            mode_of_payment = validated_data['mode_of_payment'],
            mobile = validated_data['mobile'],
            status = validated_data['status'],
        )
        pay.save()
        return pay