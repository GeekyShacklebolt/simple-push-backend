# Third party libraries
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Local imports
from apps.subscriptions.serializers import SubscriptionSerializer
from ..services.subscription_service import SubscriptionService


class SubscriptionView(APIView):

    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subscription = SubscriptionService.create_subscription(data=serializer.validated_data)
        return Response(SubscriptionSerializer(instance=subscription).data, status=status.HTTP_201_CREATED)
