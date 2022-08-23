from rest_framework import serializers

from apps.subscriptions.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            "id",
            "push_service_url",
            "public_key",
            "auth_key",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]
