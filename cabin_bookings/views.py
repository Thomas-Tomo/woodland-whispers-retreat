from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views import generic, View
from .forms import BookingForm
from .models import Cabin, Booking


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
            return redirect('booking_success', cabin_id=cabin.id, booking_id=booking.id)  # noqa
    else:
        form = BookingForm()

    context = {'cabin': cabin, 'form': form}
    return render(request, 'my_booking.html', context)


def booking_success(request, cabin_id, booking_id):
    cabin = get_object_or_404(Cabin, id=cabin_id)
    booking = get_object_or_404(Booking, id=booking_id)
    num_guests = booking.num_guests
    check_in_date = booking.check_in_date
    check_out_date = booking.check_out_date

    context = {'cabin': cabin, 'booking': booking, 'num_guests': num_guests, 'check_in_date': check_in_date, 'check_out_date': check_out_date}  # noqa
    return render(request, 'booking_success.html', context)


def booking_overview(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking_overview.html', {'bookings': bookings})


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_overview')
    else:
        form = BookingForm(instance=booking)
        context = {'form': form, 'booking': booking}

    return render(request, 'edit_booking.html', context)
