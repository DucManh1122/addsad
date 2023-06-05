from user_model.models import user_registration
from rest_framework import serializers

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_registration
        fields = ('email','password')
    def validate(self, attrs):
        user = user_registration.objects.filter(email= attrs['email'],password=attrs['password'])
        if not user:
            raise serializers.ValidationError({"status":"Failed","message":"Thông tin đăng nhập không chính xác"})
        return attrs