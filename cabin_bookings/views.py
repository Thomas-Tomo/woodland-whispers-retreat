from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.core.paginator import Paginator
from django.views import generic, View
from .forms import BookingForm
from .models import Cabin


# Create your views here.


class Home(generic.TemplateView):
    template_name = 'index.html'


def cabin_list(request):
    cabins = Cabin.objects.all()
    return render(request, 'index.html', {'cabins': cabins})


def cabin_booking(request):
    all_cabins = Cabin.objects.all()
    paginator = Paginator(all_cabins, 6)  # Display 6 cabins per page
    page_number = request.GET.get('page')
    cabins = paginator.get_page(page_number)

    return render(request, 'cabin_booking.html', {'cabins': cabins})


def booking_create(request, cabin_id):
    cabin = Cabin.objects.get(id=cabin_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.cabin = cabin
            booking.user = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()

    context = {'cabin': cabin, 'form': form}
    return render(request, 'booking.html', context)
