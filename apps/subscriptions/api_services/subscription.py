# Local imports
from ..services.subscription_service import SubscriptionService


class SubscriptionAPIService:

    @classmethod
    def get_push_subscription_data(cls, subscription_id):
        """
        Method to return push subscription data in a predefined format accepted by a webpush library.

        :param subscription_id: ID of the subscription model object
        :return: Dictionary formatted as per push subscription format
        """
        subscription_obj = SubscriptionService.get_subscription_by_id(subscription_id=subscription_id)
        return SubscriptionService.prepare_push_subscription_data(subscription_obj)

    @classmethod
    def get_subscribers_ids(cls):
        """Method to return queryset of IDs of all the subscribers model objects."""
        return SubscriptionService.get_ids_of_all_subscribers()

    @classmethod
    def get_subscription_by_id(cls, subscription_id):
        """Method to return subscriber model object for the given ID"""
        return SubscriptionService.get_subscription_by_id(subscription_id=subscription_id)
