# Generated by Django 3.2.19 on 2023-07-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_bookings', '0007_auto_20230705_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cabin',
            name='amenities',
        ),
        migrations.AddField(
            model_name='booking',
            name='cave_exploration',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='cave_exploration_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AddField(
            model_name='booking',
            name='cave_exploration_tickets',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='kayak_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AddField(
            model_name='booking',
            name='kayak_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='rent_kayak',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Amenity',
        ),
    ]
