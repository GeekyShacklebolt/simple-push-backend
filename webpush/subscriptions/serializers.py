from rest_framework import serializers

from .models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            "id",
            "push_service_url",
            "subscription_public_key",
            "subscription_auth",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]
