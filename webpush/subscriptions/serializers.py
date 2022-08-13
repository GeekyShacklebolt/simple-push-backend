from rest_framework import serializers

from .models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            "push_service_url",
            "subscription_auth",
            "subscription_secret",
        ]
