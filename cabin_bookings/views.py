from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from datetime import date
from django.utils import timezone
import json
from django.views import generic, View
from .forms import BookingForm
from django.db.models import Q
from .models import Cabin, Booking, Amenity


# Create your views here.


class Home(generic.TemplateView):
    template_name = 'index.html'


def contact_view(request):
    return render(request, 'contact.html')


def cabin_list(request):
    cabins = Cabin.objects.all()
    return render(request, 'index.html', {'cabins': cabins})


def cabin_booking(request):
    all_cabins = Cabin.objects.all().prefetch_related('amenities')
    paginator = Paginator(all_cabins, 6)  # Display 6 cabins per page
    page_number = request.GET.get('page')
    cabins = paginator.get_page(page_number)

    return render(request, 'cabin_booking.html', {'cabins': cabins})


@login_required
def booking_create(request, cabin_id):
    cabin = Cabin.objects.get(id=cabin_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.cabin = cabin
            booking.user = request.user

            num_guests = form.cleaned_data['num_guests']
            if num_guests <= 0:
                form.add_error(
                    'num_guests',
                    "The number of guests must be greater than zero."
                )
                messages.warning(
                    request,
                    "The number of guests must be greater than zero."
                )
            elif num_guests > booking.cabin.max_guests:
                form.add_error(
                    'num_guests',
                    "Exceeds maximum guests allowed."
                )
                messages.warning(
                    request,
                    "Exceeds maximum guests allowed."
                )
            else:
                check_in_date = form.cleaned_data['check_in_date']
                check_out_date = form.cleaned_data['check_out_date']
                today = timezone.now().date()

                if check_in_date < today:
                    form.add_error(
                        'check_in_date',
                        "Please select a future check-in date."
                    )
                    messages.warning(
                        request,
                        "Please select a future check-in date."
                    )
                elif check_out_date < check_in_date:
                    form.add_error(
                        'check_out_date',
                        "Check-out date can't be earlier than check-in date."
                    )
                    messages.warning(
                        request,
                        "Check-out date can't be earlier than check-in date."
                    )
                elif check_in_date == check_out_date:
                    form.add_error(
                        'check_out_date',
                        "Check-out date can't be the same as check-in date."
                    )
                    messages.warning(
                        request,
                        "Check-out date can't be the same as check-in date."
                    )
                else:
                    existing_bookings = Booking.objects.filter(
                        cabin=cabin,
                        check_in_date__lte=check_out_date,
                        check_out_date__gte=check_in_date,
                    )
                    if existing_bookings.exists():
                        form.add_error(
                            None,
                            "Cabin already booked for the selected dates"
                        )
                        messages.warning(
                            request,
                            "Cabin already booked for the selected dates"
                        )
                    else:
                        cave_exploration_tickets = form.cleaned_data.get(
                                                   'cave_exploration_tickets')
                        kayak_rentals = form.cleaned_data.get('kayak_rentals')

                    if cave_exploration_tickets and cave_exploration_tickets < 0:  # noqa
                        form.add_error(
                            'cave_exploration_tickets',
                            "Cave exploration tickets can't be negative."
                        )
                        messages.warning(
                            request,
                            "Cave exploration tickets can't be negative."
                        )

                    if kayak_rentals and kayak_rentals < 0:
                        form.add_error(
                            'kayak_rentals',
                            "The number of kayak rentals cannot be negative."
                        )
                        messages.warning(
                            request,
                            "The number of kayak rentals cannot be negative."
                        )

                    if not form.errors:
                        booking.save()
                        messages.success(
                            request,
                            "New booking created successfully."
                        )
                        return redirect(
                            'booking_success',
                            cabin_id=cabin.id,
                            booking_id=booking.id
                        )
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    if field != '__all__':
                        messages.warning(
                            request,
                            f"{form[field].label}: {error}"
                        )
    else:
        form = BookingForm()

    booked_dates = Booking.objects.filter(cabin=cabin).values_list(
        'check_in_date',
        'check_out_date'
    )

    booked_dates_str = [
        [str(check_in_date), str(check_out_date)]
        for check_in_date, check_out_date in booked_dates
    ]

    context = {
        'cabin': cabin,
        'form': form,
        'booked_dates_json': json.dumps(booked_dates_str),
    }
    return render(request, 'my_booking.html', context)


@login_required
def booking_success(request, cabin_id, booking_id):
    cabin = get_object_or_404(Cabin, id=cabin_id)
    booking = get_object_or_404(Booking, id=booking_id)
    num_guests = booking.num_guests
    check_in_date = booking.check_in_date
    check_out_date = booking.check_out_date

    context = {
        'cabin': cabin,
        'booking': booking,
        'num_guests': num_guests,
        'check_in_date': check_in_date,
        'check_out_date': check_out_date,
    }
    return render(request, 'booking_success.html', context)


@login_required
def booking_overview(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking_overview.html', {'bookings': bookings})


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booked_dates = Booking.objects.filter(cabin=booking.cabin).exclude(id=booking_id)  # noqa

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            num_guests = form.cleaned_data['num_guests']
            if num_guests <= 0:
                form.add_error(
                    'num_guests',
                    "The number of guests must be greater than zero.")
                messages.warning(
                    request,
                    "The number of guests must be greater than zero.")
            elif num_guests > booking.cabin.max_guests:
                form.add_error(
                    'num_guests',
                    "Exceeds maximum guests allowed.")
                messages.warning(
                    request,
                    "Exceeds maximum guests allowed.")
            else:
                check_in_date = form.cleaned_data['check_in_date']
                check_out_date = form.cleaned_data['check_out_date']
                today = timezone.now().date()

                if check_in_date < today:
                    form.add_error(
                        'check_in_date',
                        "Please select a future check-in date.")
                    messages.warning(
                        request,
                        "Please select a future check-in date.")
                elif check_out_date < check_in_date:
                    form.add_error(
                        'check_out_date',
                        "Check-out date can't be earlier than check-in date.")
                    messages.warning(
                        request,
                        "Check-out date can't be earlier than check-in date.")
                    form.add_error(
                        'check_out_date',
                        "Check-out date can't be the same as check-in date.")
                    messages.warning(
                        request,
                        "Check-out date can't be the same as check-in date.")
                else:
                    overlapping_bookings = booked_dates.filter(
                        check_in_date__lte=check_out_date,
                        check_out_date__gte=check_in_date
                    )

                    if overlapping_bookings.exists():
                        form.add_error(
                            None,
                            "Cabin already booked for the selected dates")
                        messages.warning(
                            request,
                            "Cabin already booked for the selected dates")
                    else:
                        form.save()
                        messages.success(
                            request,
                            "Booking updated successfully.")
                        return redirect('booking_overview')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    if field != '__all__':
                        messages.warning(
                            request,
                            f"{form[field].label}: {error}")
    else:
        form = BookingForm(instance=booking)

    booked_dates = booked_dates.values_list('check_in_date', 'check_out_date')
    booked_dates_str = [[str(check_in_date),
                        str(check_out_date)] for check_in_date,
                        check_out_date in booked_dates]

    context = {
        'form': form,
        'booking': booking,
        'booked_dates': booked_dates,
        'booked_dates_json': json.dumps(booked_dates_str),
    }

    return render(request, 'edit_booking.html', context)


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking deleted successfully.")
        return redirect('booking_overview')

    return render(request, 'delete_booking.html', {'booking': booking})
