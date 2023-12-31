# Generated by Django 5.0 on 2024-01-05 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bard', '0035_userprofile_confirmation_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='test',
            name='math_topic',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='confirmation_code',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_confirmed',
        ),
        migrations.AddField(
            model_name='question',
            name='math_topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bard.mathtopic'),
        ),
        migrations.AlterField(
            model_name='test',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
