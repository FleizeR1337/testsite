# Generated by Django 5.0 on 2024-01-17 15:45

import bard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bard', '0044_delete_confirmationcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='date_taken',
            field=models.DateTimeField(default=bard.models.get_default_date_taken),
        ),
    ]