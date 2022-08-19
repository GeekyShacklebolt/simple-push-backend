# Third party libraries
from django.urls import reverse
from unittest.mock import patch
from rest_framework import status
from rest_framework.test import APITestCase


class NotificationTest(APITestCase):

    @patch("webpush.notifications.api.spawn_webpush_requests_task.delay")
    def test_accepting_notification_data(self, mocked_webpush_task):
        url = reverse("notifications-list")
        data = {
            "title": "new title",
            "description": "test description",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), data)
        mocked_webpush_task.assert_called_once()

        # Test invalid body returns 400 Bad Request
        data = {
            "title": None,  # Title can not be None
            "description": "test description",
        }
        mocked_webpush_task.reset_mock()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        mocked_webpush_task.assert_not_called()
