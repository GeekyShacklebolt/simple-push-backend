"""simple_push URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import include

from simple_push.notifications.api import NotificationViewSet
from simple_push.subscriptions.api import SubscriptionViewSet

default_router = DefaultRouter(trailing_slash=False)

default_router.register("api/notifications", viewset=NotificationViewSet, basename="notifications")
default_router.register("api/subscriptions", viewset=SubscriptionViewSet, basename="subscriptions")

urlpatterns = default_router.urls

urlpatterns += [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
]
