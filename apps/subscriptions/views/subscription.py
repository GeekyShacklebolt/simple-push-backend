from rest_framework import viewsets, mixins

from apps.subscriptions.serializers import SubscriptionSerializer
from apps.subscriptions.models import Subscription


class SubscriptionViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):

    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
