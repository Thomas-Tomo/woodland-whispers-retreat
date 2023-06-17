from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from .models import Cabin


# Create your views here.


class Home(generic.TemplateView):
    template_name = 'index.html'


def cabin_list(request):
    cabins = Cabin.objects.all()
    return render(request, 'index.html', {'cabins': cabins})
