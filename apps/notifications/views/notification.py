# Third party libraries
from rest_framework.decorators import action
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

# Local import
from apps.notifications.serializers import NotificationSerializer
from apps.notifications.tasks import spawn_webpush_requests_task
from apps.notifications.models import Notification


class NotificationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):

    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=["POST"], detail=True)
    def send(self, request, pk=None):
        instance = self.get_object()
        spawn_webpush_requests_task.delay(notification_id=instance.id)
        return Response({"success": True}, status=status.HTTP_200_OK)
