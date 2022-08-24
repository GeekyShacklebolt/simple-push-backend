# Third party libraries
import celery

# Local imports
from apps.notifications.services.webpush_service import WebPushService


@celery.shared_task()
def trigger_webpush_request_task(notification_data, subscription_id):
    """Task to trigger webpush request for an individual subscriber."""
    WebPushService.send_webpush_request(subscription_id=subscription_id, notification_data=notification_data)
