from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class ExploreUsers(APIView):

    def get(self, request, format=None):

        last_five_user = models.User.objects.all().order_by('-data_joined')[:5]

        serializer = serializers.ExploreUsers(last_five_user, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)