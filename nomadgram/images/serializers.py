from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
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

class ImageSerializer(TaggitSerializer, serializers.ModelSerializer):

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
            'tags'
            'created_at'
        )
class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Like
        fields = (
            'creator',
        )

class InputImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Image
        fields = (
            'file',
            'location',
            'caption',
        )