# Generated by Django 4.2.4 on 2023-10-16 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0007_alter_appointment_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='time',
        ),
    ]