import json


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
