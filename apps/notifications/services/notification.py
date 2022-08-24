# Standard library
import json

# Local imports
from ..models.notification import Notification
from ..tasks import trigger_webpush_request_task
from apps.subscriptions.api_services import SubscriptionAPIService


class NotificationService:

    @classmethod
    def prepare_and_get_notification_data(cls, notification_obj):
        """Method to prepare data for notification to display

        :param notification_obj: Notification model object
        :return: Data to display in the notification
        """
        data = {
            "title": notification_obj.title,
            "description": notification_obj.description,
        }
        return json.dumps(data)

    @classmethod
    def get_notification_by_id(cls, notification_id):
        """Method to return Notification model object for the given ID

        :param notification_id: ID of the Notification model object
        :return: Notification model object
        """

        return Notification.objects.get(id=notification_id)

    @classmethod
    def send_notification_to_all_subscribers(cls, notification_id):
        """Service to spawn multiple celery tasks to send web push requests for each subscriber in background

        :param notification_id: ID of the notification model object
        :return: None
        """

        notification = cls.get_notification_by_id(notification_id=notification_id)
        notification_data = cls.prepare_and_get_notification_data(notification_obj=notification)
        subscription_ids_qs = SubscriptionAPIService.get_subscribers_ids()
        for subscription_id in subscription_ids_qs:
            trigger_webpush_request_task.delay(notification_data, subscription_id)  ## async apply

    @classmethod
    def create_notification(cls, data):
        """Service to create new Notification model objects

        :param data: Data to create a Notification object
        """
        return Notification.objects.create(**data)

    @classmethod
    def get_all_notifications(cls):
        """Service to return queryset of all the notifications objects"""
        return Notification.objects.all()
