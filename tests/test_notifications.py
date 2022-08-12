from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class NotificationTest(APITestCase):

    def test_accepting_notification_data(self):
        url = reverse("notifications-list")
        data = {
            "title": "new title",
            "description": "test description",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), data)
