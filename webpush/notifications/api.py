# Third party libraries
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

# Local import
from .serializers import NotificationSerializer
from .tasks import spawn_webpush_requests_task
from .services import prepare_notification_data
from .models import Notification


class NotificationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):

    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        notification_data = prepare_notification_data(serializer.validated_data)
        spawn_webpush_requests_task.delay(notification_data=notification_data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
