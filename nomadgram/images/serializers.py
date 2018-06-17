from rest_framework import serializers
from . import models
from nomadgram.users import models as user_models

class SmallImageSerialier(serializers.ModelSerializer):
    """ used for the notification """

    class Meta:
        model = models.Image
        field= (
            'file'
        )

class CountImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'comment_count',
            'like_count',
        )

class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.User;
        fields = (
            'username',
            'profile_image'
        )

class CommentSerializer(serializers.ModelSerializer):

    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator'
        )

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):

    creator = FeedUserSerializer()
    comments = CommentSerializer(many=True)

    class Meta:
        model = models.Image
        fields = (
            'location',
            'caption',
            'comments',
            'like_count',
            'creator',
            'created_at'
            'tags'
        )
class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Like
        fields = (
            'creator',
        )