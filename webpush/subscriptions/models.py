import uuid

from django.db import models


class Subscription(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    push_service_url = models.CharField("Push Service URL", null=False, blank=False, max_length=255)
    public_key = models.CharField(
        "Subscription Public Key", null=False, blank=False, max_length=200, help_text="P256DH Key"
    )
    auth_key = models.CharField(
        "Subscription Auth Key",
        null=False,
        blank=False,
        max_length=100,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "subscription"
        verbose_name_plural = "subscriptions"
        ordering = ("-created_at",)
