# Third party libraries
import celery
from django.conf import settings

# Local imports
from simple_push.subscriptions.models import Subscription
from simple_push.notifications.models import Notification
from simple_push.subscriptions.services import prepare_push_subscription_data
from simple_push.notifications.webpush_client import WebPushClient
from simple_push.notifications.services import prepare_notification_data

webpush_client = WebPushClient(
    vapid_private_key=settings.VAPID["PRIVATE_KEY"],
    vapid_claim_email=settings.VAPID["EMAIL"],
    notification_expire_after_mins=settings.NOTIFICATION_EXPIRE_AFTER_MINS,
)


@celery.shared_task()
def spawn_webpush_requests_task(notification_id):
    """
    Task to trigger simple_push requests to all the subscribers. This is the Parent task that spawns multiple child tasks
    to make individual simple_push requests for each subscriber.
    """
    notification = Notification.objects.get(id=notification_id)
    notification_data = prepare_notification_data(notification_obj=notification)
    subscription_ids_qs = Subscription.objects.values_list("id", flat=True)
    for subscription_id in subscription_ids_qs:
        trigger_webpush_request_task.delay(notification_data, subscription_id)


@celery.shared_task()
def trigger_webpush_request_task(notification_data, subscription_id):
    """Task to trigger simple_push request for an individual subscriber."""
    subscription = Subscription.objects.get(id=subscription_id)
    webpush_client.make_web_push_request(
        subscription_id=subscription_id,
        push_subscription_data=prepare_push_subscription_data(subscription_obj=subscription),
        notification_data=notification_data,
    )
