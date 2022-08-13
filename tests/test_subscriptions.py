from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class NotificationTest(APITestCase):

    def test_accepting_notification_data(self):
        url = reverse("subscriptions-list")
        data = {
            "push_service_url": "https://some.pushservice.com/test",
            "client_private_key": "BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=",
            "client_public_key": "FPssNDTKnInHVndSTdbKFw==",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_keys = list(data.keys())
        expected_keys.extend(["id", "created_at"])
        self.assertEqual(set(expected_keys).issubset(set(response.json().keys())))
