from rest_framework import serializers
from .models import Clothe

class ClotheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothe
        fields=('name','made_in','amount','description','price','category')
    def validate(self, attrs):
        if not (attrs['made_in'] and attrs['name'] and attrs['amount'] and attrs['description'] and attrs['price'] and attrs['category']):
            raise serializers.ValidationError({"status":"failed","message":"All fields are mandatory."})
        try:
            int(attrs['amount'])
            float(attrs['price'])
        except:
            raise serializers.ValidationError({"status":"Failed","message":"Vui lòng nhập đúng định dạng dữ liệu"})
        return attrs
    def create(self, validated_data):
        clothe = Clothe.objects.create(
            name = validated_data['name'],
            made_in = validated_data['made_in'],
            amount = int(validated_data['amount']),
            description =  validated_data['description'],
            price = float(validated_data['price']),
            category =  validated_data['category'],
        )
        clothe.save()
        return clothe
    
class ClotheSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Clothe
        fields='__all__'
    