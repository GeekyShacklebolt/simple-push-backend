# Third party libraries
from django.test import TestCase
from django_dynamic_fixture import G

# Local imports
from webpush.notifications.models import Notification
from webpush.notifications.services import prepare_notification_data


class NotificationServiceTest(TestCase):
    title = "test title"
    description = "test description"

    def setUp(self):
        self.subscription1 = G(
            Notification,
            title=self.title,
            description=self.description,
        )

    def test_prepare_notification_data(self):
        actual_result = prepare_notification_data(notification_obj=self.subscription1)
        expected_result = f"{self.title} - {self.description}"
        self.assertEqual(actual_result, expected_result)
