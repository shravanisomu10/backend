# Generated by Django 4.2.4 on 2023-10-16 02:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_remove_appointment_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='time',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
