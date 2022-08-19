from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import NotificationSerializer
from .tasks import spawn_webpush_requests_task
from .services import prepare_notification_data


class NotificationViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            notification_data = prepare_notification_data(serializer.validated_data)
            spawn_webpush_requests_task.delay(notification_data=notification_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
