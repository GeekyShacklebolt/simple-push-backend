# Third party libraries
import pytest
from django.urls import reverse
from django_dynamic_fixture import G
from unittest.mock import patch
from rest_framework import status
from rest_framework.test import APITestCase

# Local imports
from apps.notifications.models import Notification

pytestmark = pytest.mark.django_db


class NotificationTest(APITestCase):
    def test_create_notifications_api(self):
        url = reverse("notifications")
        data = {
            "title": "new title",
            "description": "test description",
        }
        expected_keys = list(data.keys())
        expected_keys.extend(["id", "created_at"])

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(set(expected_keys).issubset(set(response.json().keys())))

        notification_obj = Notification.objects.all().first()
        self.assertEqual(notification_obj.title, data["title"])
        self.assertEqual(notification_obj.description, data["description"])

    def test_create_notifications_api_raises_bad_request(self):
        url = reverse("notifications")
        # Test invalid body returns 400 Bad Request
        data = {
            "title": None,  # Title can not be None
            "description": "test description",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_notifications_api(self):
        url = reverse("notifications")
        response = self.client.get(url)
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_data), 0)

        # Create a new notification object
        new_notification = G(Notification)

        response = self.client.get(url)
        response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]["id"], str(new_notification.id))

    @patch("apps.notifications.services.notification.NotificationService.send_notification_to_all_subscribers")
    def test_notifications_send_api(self, mocked_webpush_requests_task):
        test_notification = G(Notification)
        url = reverse("notifications-send", kwargs={"pk": test_notification.id})
        response = self.client.post(url)
        mocked_webpush_requests_task.assert_called_once_with(notification_id=test_notification.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
