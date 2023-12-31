# Generated by Django 3.2.19 on 2023-06-20 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cabin_bookings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('num_guests', models.PositiveIntegerField()),
                ('cabin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin_bookings.cabin')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
