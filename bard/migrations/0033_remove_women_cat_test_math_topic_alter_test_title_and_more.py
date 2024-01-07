# Generated by Django 5.0 on 2024-01-04 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bard', '0032_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='women',
            name='cat',
        ),
        migrations.AddField(
            model_name='test',
            name='math_topic',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='bard.mathtopic'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='test',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Women',
        ),
    ]