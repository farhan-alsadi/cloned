# Generated by Django 2.2.4 on 2024-02-17 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helios_auth', '0004_auto_20240214_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='random_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='random_2',
            field=models.TextField(blank=True, null=True),
        ),
    ]
