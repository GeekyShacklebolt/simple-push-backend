import logging

# Third party libraries
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Local import
from apps.notifications.serializers import NotificationSerializer
from apps.notifications.services import NotificationService

logger = logging.getLogger(__name__)


class NotificationView(APIView):

    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        notification = NotificationService.create_notification(data=serializer.validated_data)
        return Response(NotificationSerializer(instance=notification).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        notifications = NotificationService.get_all_notifications()
        notification_list = [NotificationSerializer(instance=notification).data for notification in notifications]
        return Response(notification_list, status=status.HTTP_200_OK)

    @action(methods=["POST"], detail=True)
    def send(self, request, pk):
        NotificationService.send_notification_to_all_subscribers(notification_id=pk)
        # instance = self.get_object()
        # spawn_webpush_requests_task.delay(notification_id=instance.id)
        return Response({"success": True}, status=status.HTTP_200_OK)
