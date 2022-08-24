# Third party libraries
from django.urls import path

# Local imports
from apps.subscriptions.views.subscription import SubscriptionView

urlpatterns = [
    path("subscriptions", SubscriptionView.as_view(), name="subscriptions"),
]
