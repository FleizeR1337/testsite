# Generated by Django 4.2.8 on 2023-12-21 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bard', '0007_test_math_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='math_topic',
        ),
    ]