from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SubscriptionTest(APITestCase):
    def test_create_subscription_api(self):
        url = reverse("subscriptions")
        data = {
            "push_service_url": "https://some.pushservice.com/test",
            "public_key": "BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=",
            "auth_key": "FPssNDTKnInHVndSTdbKFw==",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_keys = list(data.keys())
        expected_keys.extend(["id", "created_at"])
        self.assertTrue(set(expected_keys).issubset(set(response.json().keys())))
