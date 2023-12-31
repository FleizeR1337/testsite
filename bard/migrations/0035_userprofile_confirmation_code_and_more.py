# Generated by Django 5.0 on 2024-01-04 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bard', '0034_remove_question_math_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
