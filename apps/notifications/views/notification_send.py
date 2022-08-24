import logging

# Third party libraries
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Local import
from apps.notifications.services import NotificationService

logger = logging.getLogger(__name__)


class NotificationSendView(APIView):

    def post(self, request, pk):
        NotificationService.send_notification_to_all_subscribers(notification_id=pk)
        return Response({"success": True}, status=status.HTTP_200_OK)
