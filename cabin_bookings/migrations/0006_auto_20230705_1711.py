# Generated by Django 3.2.19 on 2023-07-05 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_bookings', '0005_auto_20230705_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cabin',
            name='amenities',
        ),
        migrations.DeleteModel(
            name='Amenities',
        ),
    ]