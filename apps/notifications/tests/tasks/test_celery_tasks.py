# Third party libraries
from django.test import TestCase
from django_dynamic_fixture import G
from unittest.mock import patch, call

# Local imports
from apps.notifications import tasks
from apps.subscriptions.api_services.subscription import SubscriptionAPIService
from apps.notifications.services import NotificationService
from apps.subscriptions.models import Subscription
from apps.notifications.models import Notification


class NotificationCeleryTaskTest(TestCase):
    def setUp(self):
        self.test_notification = G(Notification)
        self.test_notification_data = NotificationService.prepare_and_get_notification_data(notification_obj=self.test_notification)
        self.subscription1 = G(Subscription)
        self.subscription2 = G(Subscription)
        self.push_subscription_data = SubscriptionAPIService.get_push_subscription_data(
            subscription_id=self.subscription1.id
        )

    @patch("apps.notifications.helpers.webpush_request.WebPushRequest.send")
    def test_trigger_webpush_request_task(self, mocked_webpush_request_send):
        tasks.trigger_webpush_request_task(
            notification_data=self.test_notification_data,
            subscription_id=self.subscription1.id,
        )
        mocked_webpush_request_send.assert_called_once_with(
            push_subscription_data=self.push_subscription_data,
            notification_data=self.test_notification_data,
        )
