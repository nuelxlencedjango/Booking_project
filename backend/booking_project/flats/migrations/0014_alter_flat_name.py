# Generated by Django 5.1.1 on 2024-09-24 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flats', '0013_remove_booking_previous_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
