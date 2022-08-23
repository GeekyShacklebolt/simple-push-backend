def prepare_push_subscription_data(subscription_obj):
    """
    Method to prepare push subscription data from subscription model object.

    :param subscription_obj: Object of Subscription model class
    :return: Dictionary formatted as per push subscription format
    """
    push_subscription_data = {
        "endpoint": subscription_obj.push_service_url,
        "keys": {
            "auth": subscription_obj.auth_key,
            "p256dh": subscription_obj.public_key,
        },
    }
    return push_subscription_data
