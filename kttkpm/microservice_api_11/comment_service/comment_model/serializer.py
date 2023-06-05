from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields=('id_user','id_product','content','category_product')
    def validate(self, attrs):
        if not (attrs['id_user'] and attrs['id_product'] and attrs['content'] and attrs['category_product']):
            raise serializers.ValidationError({"status":"failed","message":"Vui lòng nhập bình luận"})
        return attrs
    def create(self, validated_data):
        comment = Comment.objects.create(
            id_user = validated_data['id_user'],
            id_product = validated_data['id_product'],
            content = validated_data['content'],
            category_product = validated_data['category_product'],
        )
        comment.save()
        return comment
    