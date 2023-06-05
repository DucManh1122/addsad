from rest_framework import serializers
from .models import shipment

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = shipment
        fields = '__all__'
    def validate(self, attrs):
        if not attrs['email']:
            raise serializers.ValidationError({"status":"Failed","message":"User data is not available"})
        elif not(attrs['fname'] and attrs['lname'] and attrs['email'] and attrs['mobile'] and attrs['address'] and attrs['product_id'] and attrs['quantity'] and attrs['payment_status'] and attrs['transaction_id'] and attrs['shipment_status']):
            raise serializers.ValidationError({"status":"Failed","message":"All fields are mandatory."})
        return attrs
    def create(self, validated_data):
        ship = shipment.objects.create(
            fname = validated_data['fname'],
            lname = validated_data['lname'],
            email = validated_data['email'],
            mobile = validated_data['mobile'],
            address = validated_data['address'],
            product_id = validated_data['product_id'],
            quantity = validated_data['quantity'],
            payment_status = validated_data['payment_status'],
            transaction_id = validated_data['transaction_id'],
            shipment_status = validated_data['shipment_status']
        )
        ship.save()
        return ship

    