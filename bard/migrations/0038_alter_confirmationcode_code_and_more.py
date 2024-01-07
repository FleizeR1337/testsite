# Generated by Django 5.0 on 2024-01-05 19:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bard', '0037_confirmationcode'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationcode',
            name='code',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='confirmationcode',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]