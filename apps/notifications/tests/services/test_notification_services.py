# Third party libraries
from django.test import TestCase
from django_dynamic_fixture import G
from unittest.mock import patch, call

# Local imports
from apps.notifications.models import Notification
from apps.notifications.services import NotificationService
from apps.subscriptions.models import Subscription


class NotificationServiceTest(TestCase):
    title = "test title"
    description = "test description"

    def setUp(self):
        self.test_notification = G(
            Notification,
            title=self.title,
            description=self.description,
        )
        self.test_notification_data = NotificationService.prepare_notification_data(
            notification_obj=self.test_notification
        )
        self.test_subscription = G(Subscription)

    def test_prepare_notification_data(self):
        actual_result = self.test_notification_data
        expected_result = f'{{"title": "{self.title}", "description": "{self.description}"}}'
        self.assertEqual(actual_result, expected_result)

    @patch("apps.notifications.tasks.trigger_webpush_request_task.delay")
    def test_sending_notification_to_all_subscribers(self, mocked_trigger_webpush_celery_task):
        NotificationService.send_notification_to_all_subscribers(notification_id=self.test_notification.id)
        assert mocked_trigger_webpush_celery_task.called
        assert mocked_trigger_webpush_celery_task.call_count == 1  # since 1 test_subscription is present in setup
        calls = [
            call(self.test_notification_data, self.test_subscription.id),
        ]
        mocked_trigger_webpush_celery_task.assert_has_calls(calls, any_order=True)

