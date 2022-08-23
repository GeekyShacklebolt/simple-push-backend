# Generated by Django 4.1 on 2022-08-19 15:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Notification",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=50, verbose_name="Title")),
                ("description", models.CharField(blank=True, max_length=100, verbose_name="Description")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "notification",
                "verbose_name_plural": "notifications",
                "ordering": ("-created_at",),
                "unique_together": {("title", "description")},
            },
        ),
    ]