from rest_framework import serializers
from .models import user_registration

class  RegisterSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length = 50)

    class Meta:
        model = user_registration
        fields = ('fname','lname','email','mobile','password','confirm_password','address')

    def validate(self, attrs):
        
        if not (attrs['fname'] and attrs['lname'] and attrs['email'] and attrs['mobile'] and attrs['password'] and attrs['confirm_password'] and attrs['address']):
            raise serializers.ValidationError({"status":"Failed","message":"All fields are mandatory."})
        elif attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"status":"Failed","message":"Password and Confirm Password should be same."})
        elif len(attrs['mobile']) != 10:
            raise serializers.ValidationError({"status":"Failed","message":"Mobile Number should be 10 digit."})
        else:
            try:
                user_registration.objects.get(email = attrs['email'])
                raise serializers.ValidationError({"status":"Failed","message":"Email đã tồn tại"})
            except user_registration.DoesNotExist:
                return attrs
    def create(self, validated_data):
        user = user_registration.objects.create(
            fname=validated_data['fname'],
            lname=validated_data['lname'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            address=validated_data['address']
        )
        user.save()
        return user