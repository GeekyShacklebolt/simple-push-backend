import uuid

from django.db import models


class Subscription(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    push_service_url = models.CharField('Push Service URL', null=False, blank=False, max_length=255)
    subscription_public_key = models.CharField(
        'Subscription Public Key',
        null=False,
        blank=False,
        max_length=200,
        help_text="P256DH Key"
    )
    subscription_auth = models.CharField(
        'Subscription Auth',
        null=False,
        blank=False,
        max_length=100,
        help_text="Auth Key"
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'subscription'
        verbose_name_plural = 'subscriptions'
        ordering = (
            '-created_at',
        )

    def __str__(self):
        return f"{self.id}"
