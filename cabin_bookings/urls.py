from . import views
from django.urls import path


urlpatterns = [
    path('', views.cabin_list, name='home'),
    path('cabin-booking/', views.cabin_booking, name='cabin_booking'),
    path('booking/<int:cabin_id>/', views.booking_create, name='booking_create'),  # noqa
]
