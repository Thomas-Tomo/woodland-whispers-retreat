# Generated by Django 3.2.19 on 2023-06-24 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_bookings', '0002_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabin',
            name='bedrooms',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cabin',
            name='num_guests',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
