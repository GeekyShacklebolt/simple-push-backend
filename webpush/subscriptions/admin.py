from django.contrib import admin

from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identification', {
            'fields': (
                'id',
            )
        }),
        ('Push Subscription Details', {
            'fields': (
                'push_service_url',
                'subscription_public_key',
                'subscription_auth',
            )
        }),
        ('Other details', {
            'fields': (
                'created_at',
            ),
        }),
    )

    readonly_fields = [
        "id",
        "push_service_url",
        "subscription_public_key",
        "subscription_auth",
        "created_at",
    ]

    list_display = [
        "id",
        "created_at",
    ]


admin.site.register(Subscription, SubscriptionAdmin)
