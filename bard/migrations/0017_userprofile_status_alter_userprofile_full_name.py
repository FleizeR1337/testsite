# Generated by Django 5.0 on 2023-12-25 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bard', '0016_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
    ]
