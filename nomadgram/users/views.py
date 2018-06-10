from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class ExploreUsers(APIView):

    def get(self, request, format=None):

        last_five_user = models.User.objects.all().order_by('-date_joined')[:5]

        serializer = serializers.ExploreUserSerializer(last_five_user, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class FollowUser(APIView):

    def post(self, request, user_id, format=None):

        user = request.user;

        try:
            user_to_follow = models.User.objects.get(id = user_id)

        except models.User.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

        user.following.add(user_to_follow)
        user.save()

        return Response(status = status.HTTP_200_OK)

class UnFollowUser(APIView):

    def post(self, request, user_id, format=None):

        user = request.user;

        try:

            delete_to_follow_user = models.User.object.get(id = user_id)

        except model.User.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
        user.following.delete(delete_to_follow_user)
        user.save()

        return Response(status = status.HTTP_200_OK)

class UserProfile(APIView):

    def get (self, request, username, format=None):
        
        try:
            target_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.UserProfileSerializer(target_user)

        return Response(data = serializer.data, status = status.HTTP_200_OK)