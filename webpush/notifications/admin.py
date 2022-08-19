from django.contrib import admin

from .models import Notification


class SubscriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identification', {
            'fields': (
                'id',
            )
        }),
        ('Push Subscription Details', {
            'fields': (
                'title',
                'description',
            )
        }),
        ('Other details', {
            'fields': (
                'created_at',
            ),
        }),
    )

    readonly_fields = [
        'id',
        'created_at',
    ]

    list_display = [
        'id',
        'created_at',
    ]


admin.site.register(Notification, SubscriptionAdmin)
