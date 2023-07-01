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
            if num_guests > cabin.max_guests:
                form.add_error('num_guests', "The number of guests exceeds the maximum allowed for this cabin.")  # noqa
                messages.warning(request, "The number of guests exceeds the maximum allowed for this cabin.")  # noqa
            else:
                check_in_date = form.cleaned_data['check_in_date']
                check_out_date = form.cleaned_data['check_out_date']
                today = timezone.now().date()

                if check_in_date < today:
                    form.add_error('check_in_date', "Please select a future check-in date.")  # noqa
                    messages.warning(request, "Please select a future check-in date.")  # noqa
                elif check_out_date < check_in_date:
                    form.add_error('check_out_date', "Check-out date cannot be earlier than the check-in date.")  # noqa
                    messages.warning(request, "Check-out date cannot be earlier than the check-in date.")  # noqa
                elif check_in_date == check_out_date:
                    form.add_error('check_out_date', "Check-out date cannot be the same as the check-in date.")  # noqa
                    messages.warning(request, "Check-out date cannot be the same as the check-in date.")  # noqa
                else:
                    # Check if the cabin is already booked for the selected dates  # noqa
                    existing_bookings = Booking.objects.filter(
                        cabin=cabin,
                        check_in_date__lte=check_out_date,
                        check_out_date__gte=check_in_date,
                    )
                    if existing_bookings.exists():
                        form.add_error(None, "The cabin is already booked for the selected dates.")  # noqa
                        messages.warning(request, "The cabin is already booked for the selected dates.")  # noqa
                    else:
                        booking.save()
                        messages.success(request, "New booking created successfully.")  # noqa
                        return redirect('booking_success', cabin_id=cabin.id, booking_id=booking.id)  # noqa
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    if field != '__all__':
                        messages.warning(request, f"{form[field].label}: {error}")  # noqa
    else:
        form = BookingForm()

    booked_dates = Booking.objects.filter(cabin=cabin).values_list('check_in_date', 'check_out_date')  # noqa

    booked_dates_str = [[str(check_in_date), str(check_out_date)] for check_in_date, check_out_date in booked_dates]  # noqa

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

    context = {'cabin': cabin, 'booking': booking, 'num_guests': num_guests, 'check_in_date': check_in_date, 'check_out_date': check_out_date}  # noqa
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
            if num_guests > booking.cabin.max_guests:
                form.add_error('num_guests', "The number of guests exceeds the maximum allowed for this cabin.")  # noqa
                messages.warning(request, "The number of guests exceeds the maximum allowed for this cabin.")  # noqa
            else:
                check_in_date = form.cleaned_data['check_in_date']
                check_out_date = form.cleaned_data['check_out_date']

                # Check for overlapping bookings for the same cabin
                overlapping_bookings = booked_dates.filter(
                    check_in_date__lte=check_out_date,
                    check_out_date__gte=check_in_date
                )

                if overlapping_bookings.exists():
                    form.add_error(None, "The cabin is already booked for the selected dates.")  # noqa
                    messages.warning(request, "The cabin is already booked for the selected dates.")  # noqa
                else:
                    form.save()
                    messages.success(request, "Booking updated successfully.")
                    return redirect('booking_overview')
        else:
            messages.warning(request, "Please select a future check-in and check-out date.")  # noqa
    else:
        form = BookingForm(instance=booking)

    context = {'form': form, 'booking': booking, 'booked_dates': booked_dates}
    return render(request, 'edit_booking.html', context)


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking deleted successfully.")
        return redirect('booking_overview')

    return render(request, 'delete_booking.html', {'booking': booking})
