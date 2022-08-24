# Third party libraries
from django.urls import path

# Local imports
from apps.notifications.views.notification import NotificationView
from apps.notifications.views.notification_send import NotificationSendView

urlpatterns = [
    path("notifications", NotificationView.as_view(), name="notifications"),
    path("notifications/<uuid:pk>/send", NotificationSendView.as_view(), name="notifications-send"),
]
