

def prepare_notification_data(request_data):
    """Temporary method to prepare notification data on the go. At the completion of Milestone 4, notification to
    trigger would be configurable via dashboard
    """
    return f"{request_data['title']} - {request_data['description']}"
