# Generated by Django 5.0 on 2024-01-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bard', '0040_tempregistration_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempregistration',
            name='confirmation_code',
            field=models.CharField(max_length=100),
        ),
    ]
