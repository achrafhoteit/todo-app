# Generated by Django 4.2.4 on 2023-08-20 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='end_date',
        ),
        migrations.AddField(
            model_name='task',
            name='deadline_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='deadline_time',
            field=models.TimeField(default='12:00'),
            preserve_default=False,
        ),
    ]
