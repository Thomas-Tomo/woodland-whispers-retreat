# Generated by Django 3.2.19 on 2023-07-05 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_bookings', '0004_rename_num_guests_cabin_max_guests'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('tour_available', models.BooleanField(default=False)),
                ('tour_price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('kayak_available', models.BooleanField(default=False)),
                ('kayak_price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
        migrations.AddField(
            model_name='cabin',
            name='amenities',
            field=models.ManyToManyField(to='cabin_bookings.Amenities'),
        ),
    ]
