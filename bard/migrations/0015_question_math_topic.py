# Generated by Django 5.0 on 2023-12-25 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bard', '0014_delete_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='math_topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bard.mathtopic'),
        ),
    ]
