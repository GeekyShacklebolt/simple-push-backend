# Third party libraries
from rest_framework import serializers

# Local imports
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "id",
            "title",
            "description",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]
