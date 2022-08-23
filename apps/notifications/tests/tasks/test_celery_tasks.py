# Third party libraries
from django.test import TestCase
from django_dynamic_fixture import G
from unittest.mock import patch, call

# Local imports
from apps.notifications import tasks
from apps.subscriptions.api_services.subscription import SubscriptionAPIServices
from apps.notifications.services import NotificationService
from apps.subscriptions.models import Subscription
from apps.notifications.models import Notification


class NotificationCeleryTaskTest(TestCase):
    def setUp(self):
        self.test_notification = G(Notification)
        self.test_notification_data = NotificationService.prepare_and_get_notification_data(notification_obj=self.test_notification)
        self.subscription1 = G(Subscription)
        self.subscription2 = G(Subscription)

    @patch("apps.notifications.tasks.trigger_webpush_request_task.delay")
    def test_spawn_webpush_requests_task(self, mocked_trigger_webpush_celery_task):
        tasks.spawn_webpush_requests_task(notification_id=self.test_notification.id)
        assert mocked_trigger_webpush_celery_task.called
        assert mocked_trigger_webpush_celery_task.call_count == 2  # since 2 subscription objects are present in setup
        calls = [
            call(self.test_notification_data, self.subscription1.id),
            call(self.test_notification_data, self.subscription2.id),
        ]
        mocked_trigger_webpush_celery_task.assert_has_calls(calls, any_order=True)

    @patch("apps.notifications.tasks.make_webpush_requests_task.webpush_client.make_web_push_request")
    def test_trigger_webpush_request_task(self, mocked_web_push_request):
        push_subscription_data = SubscriptionAPIServices.prepare_and_get_push_subscription_data(subscription_obj=self.subscription1)
        tasks.trigger_webpush_request_task(
            notification_data=self.test_notification_data,
            subscription_id=self.subscription1.id,
        )
        mocked_web_push_request.assert_called_once_with(
            subscription_id=self.subscription1.id,
            push_subscription_data=push_subscription_data,
            notification_data=self.test_notification_data,
        )
