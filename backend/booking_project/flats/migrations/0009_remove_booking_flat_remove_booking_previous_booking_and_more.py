# Generated by Django 5.1.1 on 2024-09-23 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flats', '0008_remove_booking_previousid_booking_previous_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='flat',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='previous_booking',
        ),
        migrations.DeleteModel(
            name='Flat',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
