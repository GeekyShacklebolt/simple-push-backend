# Standard libraries
import uuid

# Third party libraries
from django.db import models


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField('Title', null=False, blank=False, max_length=50)
    description = models.CharField('Description', null=False, blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'
        ordering = (
            '-created_at',
        )
