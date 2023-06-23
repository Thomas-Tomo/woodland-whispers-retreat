from . import views
from django.urls import path


urlpatterns = [
    path('', views.cabin_list, name='home'),
    path('cabin-booking/', views.cabin_booking, name='cabin_booking'),
    path('booking/<int:cabin_id>/', views.booking_create, name='my_booking'),  # noqa
    path('booking/success/<int:cabin_id>/<int:booking_id>/', views.booking_success, name='booking_success'),  # noqa
    path('booking-overview/', views.booking_overview, name='booking_overview'),
    path('booking/edit/<int:booking_id>/', edit_booking, name='edit_booking'),
]
