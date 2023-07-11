from django.contrib import admin
from .models import Cabin, Booking, Amenity


class BookingAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Booking model.

    This class defines the custom admin interface for the Booking model.

    It specifies the list of fields to be displayed in the admin list
    view for Booking objects.
    """
    list_display = ['id',
                    'user',
                    'cabin',
                    'check_in_date',
                    'check_out_date',
                    'cave_exploration_tickets',
                    'kayak_rentals']


# Registering the models in the admin site
admin.site.register(Amenity)
admin.site.register(Cabin)
admin.site.register(Booking, BookingAdmin)
