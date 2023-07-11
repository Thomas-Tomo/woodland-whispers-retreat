from django import forms
from .models import Booking, Amenity
from django.core.validators import MinValueValidator


class BookingForm(forms.ModelForm):
    """
    A form for creating or updating a booking.

    This form is used for creating or updating a booking

    The form includes validators to ensure that the minimum value
    for num_guests,cave_exploration_tickets, and kayak_rentals is 0 or 1.
    """
    num_guests = forms.IntegerField(validators=[MinValueValidator(1)])
    # Optional field for cave exploration tickets
    cave_exploration_tickets = forms.IntegerField(
                               validators=[MinValueValidator(0)],
                               required=False)
    # Optional field for kayak rentals
    kayak_rentals = forms.IntegerField(validators=[MinValueValidator(0)],
                                       required=False)

    class Meta:
        model = Booking
        fields = ['check_in_date',
                  'check_out_date',
                  'num_guests',
                  'cave_exploration_tickets',
                  'kayak_rentals']
