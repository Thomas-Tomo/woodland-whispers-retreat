from django import forms
from .models import Booking
from django.core.validators import MinValueValidator


class BookingForm(forms.ModelForm):
    num_guests = forms.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        model = Booking
        fields = ['check_in_date', 'check_out_date', 'num_guests']
