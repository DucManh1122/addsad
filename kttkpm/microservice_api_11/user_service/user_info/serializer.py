from user_model.models import user_registration
from rest_framework import serializers

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_registration
        fields = '__all__'