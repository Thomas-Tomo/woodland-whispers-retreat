from django import forms
from .models import Booking, Amenity
from django.core.validators import MinValueValidator


class BookingForm(forms.ModelForm):
    num_guests = forms.IntegerField(validators=[MinValueValidator(1)])
    cave_exploration_tickets = forms.IntegerField(
                               validators=[MinValueValidator(0)],
                               required=False)
    kayak_rentals = forms.IntegerField(validators=[MinValueValidator(0)],
                                       required=False)

    class Meta:
        model = Booking
        fields = ['check_in_date',
                  'check_out_date',
                  'num_guests',
                  'cave_exploration_tickets',
                  'kayak_rentals']
