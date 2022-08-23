# Third party libraries
from django.test import TestCase
from django_dynamic_fixture import G

# Local imports
from apps.notifications.models import Notification
from apps.notifications.services import NotificationService


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
        actual_result = NotificationService.prepare_and_get_notification_data(notification_obj=self.subscription1)
        expected_result = f'{{"title": "{self.title}", "description": "{self.description}"}}'
        self.assertEqual(actual_result, expected_result)
