from . import views
from django.urls import path
from django.conf.urls import handler404
from django.conf.urls import handler500
from .views import custom_handler404, custom_handler500

# Url Mapping
urlpatterns = [
    # Open Home and Contact page
    path('', views.cabin_list, name='home'),
    path('contact/', views.contact_view, name='contact'),

    # Create, Read, Update and Delete Cabin Bookings
    path('cabin-booking/', views.cabin_booking, name='cabin_booking'),
    path('booking/<int:cabin_id>/',
         views.booking_create, name='my_booking'),
    path('booking/success/<int:cabin_id>/<int:booking_id>/',
         views.booking_success, name='booking_success'),
    path('booking-overview/',
         views.booking_overview, name='booking_overview'),
    path('booking/edit/<int:booking_id>/',
         views.edit_booking, name='edit_booking'),
    path('booking/<int:booking_id>/delete/',
         views.delete_booking, name='delete_booking'),
]

handler404 = custom_handler404
handler500 = custom_handler500
