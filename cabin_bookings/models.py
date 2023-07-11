from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.utils import timezone


class Amenity(models.Model):
    """
    Add a new amenity as Admin in admin panel
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Cabin(models.Model):
    """
    Add a new cabin as Admin in admin panel
    """
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
    """
    Cabin Booking
    This class handles the information related to a booking made by a user
    for a specific cabin. It stores details such as the booked cabin,
    the user who made the booking, check-in and check-out dates,
    the number of guests, optional quantities of cave exploration
    tickets and kayak rentals, and the total price.

    """
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
