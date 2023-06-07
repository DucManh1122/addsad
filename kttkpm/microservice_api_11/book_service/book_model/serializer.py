from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=('name','author','amount','description','price','category')
    def validate(self, attrs):
        if not (attrs['author'] and attrs['name'] and attrs['amount'] and attrs['description'] and attrs['price'] and attrs['category']):
            raise serializers.ValidationError({"status":"failed","message":"All fields are mandatory."})
        try:
            int(attrs['amount'])
            float(attrs['price'])
        except:
            raise serializers.ValidationError({"status":"Failed","message":"Vui lòng nhập đúng định dạng dữ liệu"})
        return attrs
    def create(self, validated_data):
        book = Book.objects.create(
            name = validated_data['name'],
            author = validated_data['author'],
            amount = int(validated_data['amount']),
            description =  validated_data['description'],
            price = float(validated_data['price']),
            category = validated_data['category'],
        )
        book.save()
        return book
    
class BookSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields='__all__'