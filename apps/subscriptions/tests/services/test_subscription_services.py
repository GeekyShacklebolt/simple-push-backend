# Third party libraries
from django.test import TestCase
from django_dynamic_fixture import G

# Local imports
from apps.subscriptions.models import Subscription
from apps.subscriptions.api_services.subscription import SubscriptionAPIService


class SubscriptionServiceTest(TestCase):
    push_service_url = "test_url"
    public_key = "test_public_key"
    auth_key = "test_auth_key"

    def setUp(self):
        self.subscription1 = G(
            Subscription,
            push_service_url=self.push_service_url,
            public_key=self.public_key,
            auth_key=self.auth_key,
        )

    def test_prepare_push_subscription_data(self):
        actual_result = SubscriptionAPIService.get_push_subscription_data(subscription_id=self.subscription1.id)
        expected_result = {
            "endpoint": self.push_service_url,
            "keys": {
                "p256dh": self.public_key,
                "auth": self.auth_key,
            },
        }
        self.assertEqual(actual_result, expected_result)
