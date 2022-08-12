from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
