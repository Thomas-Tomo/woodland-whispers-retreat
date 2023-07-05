# Generated by Django 3.2.19 on 2023-07-05 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_bookings', '0011_auto_20230705_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='include_cave_exploration',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='include_kayak_rental',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='num_kayaks',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='num_tickets',
        ),
        migrations.RemoveField(
            model_name='cabin',
            name='amenities',
        ),
        migrations.DeleteModel(
            name='Amenities',
        ),
    ]
