

def prepare_notification_data(notification_obj):
    """Method to prepare data for notification to display

    :param notification_obj: Notification model object
    :return: Data to display in the notification
    """
    return f"{notification_obj.title} - {notification_obj.description}"
