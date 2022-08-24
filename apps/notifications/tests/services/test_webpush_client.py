# Standard Libraries
import uuid

# Third party libraries
import pytest
from django.test import TestCase
from unittest.mock import patch, PropertyMock
from pywebpush import WebPushException

# Local imports
from apps.notifications.helpers.webpush_request import WebPushRequest
from apps.notifications.common.exceptions import WebPushRequestException


class WebPushLibraryWrapperTest(TestCase):
    def setUp(self):
        self.vapid_private_key = "fake_private_key"
        self.vapid_claim_email = "test@email.com"
        self.notification_expire_after_mins = 1

        self.subscription_id = uuid.uuid4()
        self.push_subscription_data = "example subscription data"
        self.notification_data = "title"

        self.webpush_request = WebPushRequest(
            vapid_private_key=self.vapid_private_key,
            vapid_claim_email=self.vapid_claim_email,
            notification_expire_after_mins=self.notification_expire_after_mins,
        )

    def test_client_initialization(self):
        self.assertEqual(self.webpush_request.vapid_private_key, self.vapid_private_key)
        self.assertEqual(self.webpush_request.vapid_claim_email, self.vapid_claim_email)
        self.assertEqual(self.webpush_request.notification_expire_after_mins, self.notification_expire_after_mins)
        self.assertEqual(set(self.webpush_request.vapid_auth_token_claims.keys()), {"exp", "sub"})
        self.assertEqual(self.webpush_request.vapid_auth_token_claims["sub"], f"mailto:{self.vapid_claim_email}")

    @patch("apps.notifications.helpers.webpush_request.webpush")
    def test_make_web_push_request(self, mocked_webpush):
        # Mocking HTTP response from library as success
        type(mocked_webpush.return_value).ok = PropertyMock(return_value=True)
        self.webpush_request.send(
            push_subscription_data=self.push_subscription_data,
            notification_data=self.notification_data,
        )
        mocked_webpush.asser_called_once_with(
            self.push_subscription_data,
            self.notification_data,
            self.vapid_private_key,
            self.webpush_request.vapid_auth_token_claims,
        )

    @patch("apps.notifications.helpers.webpush_request.webpush", side_effect=WebPushException(message="Error!"))
    def test_make_web_push_request_catches_exception(self, mocked_webpush):

        with pytest.raises(WebPushRequestException) as custom_exc:
            with pytest.raises(WebPushException) as lib_exc:
                self.webpush_request.send(
                    push_subscription_data=self.push_subscription_data,
                    notification_data=self.notification_data,
                )
        self.assertIsNotNone(lib_exc)
        self.assertIsNotNone(custom_exc)
        assert "Web Push Request Failed." in str(custom_exc.value)

        mocked_webpush.assert_called_once_with(
            self.push_subscription_data,
            self.notification_data,
            self.vapid_private_key,
            self.webpush_request.vapid_auth_token_claims,
        )

    @patch("apps.notifications.helpers.webpush_request.webpush")
    def test_make_web_push_request_raises_custom_exception_on_failure(self, mocked_webpush):
        # Mocking HTTP response from library as not OK
        type(mocked_webpush.return_value).ok = PropertyMock(return_value=False)
        with pytest.raises(WebPushRequestException) as custom_exc:
            self.webpush_request.send(
                push_subscription_data=self.push_subscription_data,
                notification_data=self.notification_data,
            )
        self.assertIsNotNone(custom_exc)
        assert "Web Push Request Failed." in str(custom_exc)

        mocked_webpush.assert_called_once_with(
            self.push_subscription_data,
            self.notification_data,
            self.vapid_private_key,
            self.webpush_request.vapid_auth_token_claims,
        )
