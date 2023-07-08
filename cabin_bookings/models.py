from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.


class Amenity(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Cabin(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = CloudinaryField('log_cabin_images')
    max_guests = models.PositiveIntegerField(default=1)
    bedrooms = models.PositiveIntegerField(default=1)
    amenities = models.ManyToManyField(Amenity)

    def __str__(self):
        return self.name


class Booking(models.Model):
    cabin = models.ForeignKey(Cabin, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_guests = models.PositiveIntegerField()
    cave_exploration_tickets = models.PositiveIntegerField(
                               default=0, null=True)
    kayak_rentals = models.PositiveIntegerField(default=0, null=True)
    total_price = models.DecimalField(
                  max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f"Booking {self.id} - Cabin: {self.cabin.name}, User: {self.user.username}"  # noqa
