# Generated by Django 5.1.1 on 2024-09-26 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flats', '0021_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin',
            field=models.DateTimeField(),
        ),
    ]
