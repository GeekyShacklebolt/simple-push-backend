# Local imports
from ..models.subscription import Subscription


class SubscriptionService:

    @classmethod
    def get_ids_of_all_subscribers(cls):
        """Service to return IDs of all of Subscriber's model objects"""
        return Subscription.objects.values_list("id", flat=True)

    @classmethod
    def prepare_push_subscription_data(cls, subscription_obj):
        """Service to prepare and return push subscription data in a predefined format"""
        push_subscription_data = {
            "endpoint": subscription_obj.push_service_url,
            "keys": {
                "auth": subscription_obj.auth_key,
                "p256dh": subscription_obj.public_key,
            },
        }
        return push_subscription_data

    @classmethod
    def get_subscription_by_id(cls, subscription_id):
        """Service to return subscriber model object for the given ID"""
        return Subscription.objects.get(id=subscription_id)

    @classmethod
    def create_subscription(cls, data):
        """Service to create new Subscription model objects

        :param data: Data to create a Subscription object
        """
        return Subscription.objects.create(**data)
