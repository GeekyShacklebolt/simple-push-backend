# Standard import
import logging

# Third party imports
from django.conf import settings

# Local imports
from apps.notifications.helpers.webpush_request import WebPushRequest
from apps.subscriptions.api_services import SubscriptionAPIService
from ..common.exceptions import WebPushRequestException

logger = logging.getLogger(__name__)


class WebPushService:
    webpush_request = WebPushRequest(
        vapid_private_key=settings.VAPID["PRIVATE_KEY"],
        vapid_claim_email=settings.VAPID["EMAIL"],
        notification_expire_after_mins=settings.NOTIFICATION_EXPIRE_AFTER_MINS,
    )

    @classmethod
    def send_webpush_request(cls, subscription_id, notification_data):
        """
        Service to trigger sending webpush request for the given subscription id and notification data.

        :param subscription_id: ID of the subscription model object
        :param notification_data: Notification data to send
        :return:
        """
        def get_log_ci():
            """Method returns Correlation-Info needed to associate an identification with a log"""
            return f"subscription ID '{subscription_id}' and notification data '{notification_data}'"

        push_subscription_data = SubscriptionAPIService.get_push_subscription_data(subscription_id=subscription_id)
        logger.info(msg=f"Attempting to send webpush request. {get_log_ci()}")
        try:
            cls.webpush_request.send(
                notification_data=notification_data,
                push_subscription_data=push_subscription_data,
            )
            logger.info(msg=f"Successfully made webpush request. {get_log_ci()}")
        except WebPushRequestException as exc:
            logger.info(msg=f"Failed to make webpush request due to exception {exc}. {get_log_ci()}")
