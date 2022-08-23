# Standard library
import logging
import datetime

# Third party libraries
from pywebpush import webpush
from pywebpush import WebPushException

# Local imports
from apps.notifications.common.exceptions import WebPushRequestException

logger = logging.getLogger(__name__)


class WebPushClient(object):
    """Class wraps pywebpush library."""

    def __init__(
        self,
        vapid_private_key,
        vapid_claim_email,
        notification_expire_after_mins,
    ):
        self.vapid_private_key = vapid_private_key
        self.vapid_claim_email = vapid_claim_email
        self.notification_expire_after_mins = notification_expire_after_mins
        self.vapid_claim_exp = self._compute_vapid_auth_token_expiry()

    @property
    def vapid_auth_token_claims(self):
        """The audience claim `aud` is not set here, because pywebpush library extracts that out on its own
        using the push service endpoint's URL coming in the push subscription data."""
        return {"sub": f"mailto:{self.vapid_claim_email}", "exp": self.vapid_claim_exp}

    def _compute_vapid_auth_token_expiry(self):
        """Method to compute VAPID auth token expiry claim.

        :return: expiry time in epoch seconds
        """

        def get_epoch_seconds(date_time):
            return int(date_time.timestamp())

        now = datetime.datetime.now()
        expire_after_mins = datetime.timedelta(minutes=self.notification_expire_after_mins)
        expiry = now + expire_after_mins

        return get_epoch_seconds(expiry)

    def make_web_push_request(self, subscription_id, push_subscription_data, notification_data):
        """Method to make simple_push request using pywebpush library.

        :param subscription_id: ID of the user's subscription obj to track in logging.
        :param push_subscription_data: PushSubscription data unique for a subscribed user
        :param notification_data: Data to display in the notification

        :return: Http Response from pywebpush.simple_push module

        :raises: WebPushRequestException if pywebpush library fails to make the simple_push request due to any reason.
        """

        def get_log_ci():
            """Method returns Correlation-Info needed to associate an identification with a log"""
            return f"subscription ID '{subscription_id}' and notification data '{notification_data}'"

        try:
            logger.info(msg=f"Attempting to make simple_push request. {get_log_ci()}")
            result = webpush(
                push_subscription_data,
                notification_data,
                self.vapid_private_key,
                self.vapid_auth_token_claims,
            )
            if result.ok:
                logger.info(msg=f"Successfully made simple_push request. {get_log_ci()}")
                return result

            logger.info(msg=f"Failed to make simple_push request. '{result.text}'. {get_log_ci()}")
            raise WebPushRequestException(f"Web Push Request Failed. {result.text}.")

        except WebPushException as exc:
            logger.info(msg=f"Failed to make simple_push request due to exception {exc}. {get_log_ci()}")
            raise WebPushRequestException(f"Web Push Request Failed. {exc}")
