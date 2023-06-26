from django.contrib import admin
from .models import Cabin, Booking

# Register your models here.

admin.site.register(Cabin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'cabin', 'check_in_date', 'check_out_date']


admin.site.register(Booking, BookingAdmin)
