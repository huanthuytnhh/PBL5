# Generated by Django 5.1.7 on 2025-04-14 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devices", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="device",
            old_name="status",
            new_name="is_on",
        ),
        migrations.AddField(
            model_name="device",
            name="device_type",
            field=models.CharField(
                choices=[
                    ("led", "LED"),
                    ("switch", "Switch"),
                    ("sensor", "Sensor"),
                    ("other", "Other"),
                ],
                default="led",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="gpio_pin",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="device",
            name="ip_address",
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
