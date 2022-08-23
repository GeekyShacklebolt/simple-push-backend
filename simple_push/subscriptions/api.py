from rest_framework import viewsets, mixins

from .serializers import SubscriptionSerializer
from .models import Subscription


class SubscriptionViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):

    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
