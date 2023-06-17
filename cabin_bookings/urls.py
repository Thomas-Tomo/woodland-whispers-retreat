from . import views
from django.urls import path


urlpatterns = [
    path('', views.cabin_list, name='home'),
]
