from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from datetime import date
from django.utils import timezone
import json
from django.views import generic, View
from .forms import BookingForm
from .models import Cabin, Booking, Amenity


class Home(generic.TemplateView):
    template_name = 'index.html'


def contact_view(request):
    return render(request, 'contact.html')


def cabin_list(request):
    """
    This function retrieves all cabins from the database and renders
    the 'index.html' template, passing the cabins as context.
    """
    cabins = Cabin.objects.all()
    return render(request, 'index.html', {'cabins': cabins})


def cabin_booking(request):
    """
    This function retrieves all cabins from the database with
    prefetched amenities, paginates the cabins to display 6 per page,
    and renders the 'cabin_booking.html' template,
    passing the paginated cabins as context.
    """
    all_cabins = Cabin.objects.all().prefetch_related('amenities')
    paginator = Paginator(all_cabins, 6)  # Display 6 cabins per page
    page_number = request.GET.get('page')
    cabins = paginator.get_page(page_number)

    return render(request, 'cabin_booking.html', {'cabins': cabins})


@login_required
def booking_create(request, cabin_id):
    """
    This function handles the creation of a new booking for the
    specified cabin. It performs form validation, checks for validation
    errors, and handles various validation cases. If the booking is
    successfully created, it redirects to the booking success page.
    """
    cabin = Cabin.objects.get(id=cabin_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Process form data and perform validations
            booking = form.save(commit=False)
            booking.cabin = cabin
            booking.user = request.user

            num_guests = form.cleaned_data['num_guests']
            if num_guests <= 0:
                # Check if the number of guests is greater than zero
                form.add_error(
                    'num_guests',
                    "The number of guests must be greater than zero."
                )
                messages.warning(
                    request,
                    "The number of guests must be greater than zero."
                )
            elif num_guests > booking.cabin.max_guests:
                # Check if the number of guests exceeds the maximum allowed
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
                    # Check if the check-in date is in the past
                    form.add_error(
                        'check_in_date',
                        "Please select a future check-in date."
                    )
                    messages.warning(
                        request,
                        "Please select a future check-in date."
                    )
                elif check_out_date < check_in_date:
                    # Check if check-out date is earlier than the check-in date
                    form.add_error(
                        'check_out_date',
                        "Check-out date can't be earlier than check-in date."
                    )
                    messages.warning(
                        request,
                        "Check-out date can't be earlier than check-in date."
                    )
                elif check_in_date == check_out_date:
                    # Check if check-in date and check-out date are the same
                    form.add_error(
                        'check_out_date',
                        "Check-out date can't be the same as check-in date."
                    )
                    messages.warning(
                        request,
                        "Check-out date can't be the same as check-in date."
                    )
                else:
                    # Check if there are any overlapping bookings
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
                        # Check additional validations
                        cave_exploration_tickets = form.cleaned_data.get(
                                                   'cave_exploration_tickets')
                        kayak_rentals = form.cleaned_data.get('kayak_rentals')

                        if cave_exploration_tickets and (
                                cave_exploration_tickets < 0 or
                                cave_exploration_tickets > num_guests):
                            form.add_error(
                                'cave_exploration_tickets',
                                "Cave exploration tickets can't be negative."
                            )
                            messages.warning(
                                request,
                                "Tickets can't exceed num of selected guests."
                            )

                        if kayak_rentals and (
                                kayak_rentals < 0 or kayak_rentals > 10):
                            form.add_error(
                                'kayak_rentals',
                                "Kayak rental ranges from 0 to 10"
                            )
                            messages.warning(
                                request,
                                "Kayak rental ranges from 0 to 10"
                            )

                        cave_exploration_tickets = cave_exploration_tickets or 0  # noqa
                        kayak_rentals = kayak_rentals or 0

                        if not form.errors:
                            duration = (check_out_date - check_in_date).days
                            # Calculate total price
                            total_price = cabin.price * duration

                            total_price += (
                                cave_exploration_tickets * Amenity.objects.get(
                                    name='Cave Exploration').price)
                            total_price += (
                                kayak_rentals * Amenity.objects.get(
                                    name='Kayak Rental').price)

                            booking.total_price = total_price
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
            # Handle form validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    if field != '__all__':
                        messages.warning(
                            request,
                            f"{form[field].label}: {error}"
                        )
    else:
        form = BookingForm()
    # Get booked dates for the cabin
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
    """
    This function retrieves the cabin and booking objects associated
    with the provided IDs. It gathers the necessary information from
    the booking object. Finally, it renders the 'booking_success.html'
    template, passing the relevant context.
    """
    cabin = get_object_or_404(Cabin, id=cabin_id)
    booking = get_object_or_404(Booking, id=booking_id)
    num_guests = booking.num_guests
    check_in_date = booking.check_in_date
    check_out_date = booking.check_out_date
    cave_exploration_tickets = booking.cave_exploration_tickets
    kayak_rentals = booking.kayak_rentals

    context = {
        'cabin': cabin,
        'booking': booking,
        'num_guests': num_guests,
        'check_in_date': check_in_date,
        'check_out_date': check_out_date,
        'cave_exploration_tickets': cave_exploration_tickets,
        'kayak_rentals': kayak_rentals,
    }
    return render(request, 'booking_success.html', context)


@login_required
def booking_overview(request):
    """
    This function retrieves all bookings associated with the currently
    logged-in user. It renders the 'booking_overview.html' template,
    passing the bookings as context.

    """
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking_overview.html', {'bookings': bookings})


@login_required
def edit_booking(request, booking_id):
    """
    This function handles the editing of an existing booking identified
    by the provided booking_id. It performs form validation, checks for
    validation errors, and handles various validation cases. If the
    booking is successfully updated, it redirects to the booking overview page.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booked_dates = Booking.objects.filter(
                   cabin=booking.cabin).exclude(id=booking_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            # Process form data and perform validations
            num_guests = form.cleaned_data['num_guests']
            if num_guests <= 0:
                # Check if the number of guests is greater than zero
                form.add_error(
                    'num_guests',
                    "The number of guests must be greater than zero."
                )
                messages.warning(
                    request,
                    "The number of guests must be greater than zero."
                )
            elif num_guests > booking.cabin.max_guests:
                # Check if the number of guests exceeds the maximum allowed
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
                    # Check if the check-in date is in the past
                    form.add_error(
                        'check_in_date',
                        "Please select a future check-in date."
                    )
                    messages.warning(
                        request,
                        "Please select a future check-in date."
                    )
                elif check_out_date < check_in_date:
                    # Check if check-out date is earlier than the check-in date
                    form.add_error(
                        'check_out_date',
                        "Check-out date can't be earlier than check-in date."
                    )
                    messages.warning(
                        request,
                        "Check-out date can't be earlier than check-in date."
                    )
                elif check_in_date == check_out_date:
                    # Check if check-in date and check-out date are the same
                    form.add_error(
                        'check_out_date',
                        "Check-out date can't be the same as check-in date."
                    )
                    messages.warning(
                        request,
                        "Check-out date can't be the same as check-in date."
                    )
                else:
                    # Check if there are any overlapping bookings
                    overlapping_bookings = booked_dates.filter(
                        check_in_date__lte=check_out_date,
                        check_out_date__gte=check_in_date
                    )

                    if overlapping_bookings.exists():
                        form.add_error(
                            None,
                            "Cabin already booked for the selected dates"
                        )
                        messages.warning(
                            request,
                            "Cabin already booked for the selected dates"
                        )
                    else:
                        # Check additional validations
                        cave_exploration_tickets = form.cleaned_data.get(
                                                   'cave_exploration_tickets')
                        kayak_rentals = form.cleaned_data.get('kayak_rentals')

                        if cave_exploration_tickets and (
                                cave_exploration_tickets < 0 or
                                cave_exploration_tickets > num_guests):
                            form.add_error(
                                'cave_exploration_tickets',
                                "Tickets can't exceed num of selected guests."
                            )
                            messages.warning(
                                request,
                                "Tickets can't exceed num of selected guests."
                            )

                        if kayak_rentals and (
                                kayak_rentals < 0 or kayak_rentals > 10):
                            form.add_error(
                                'kayak_rentals',
                                "Kayak rental ranges from 0 to 10"
                            )
                            messages.warning(
                                request,
                                "Kayak rental ranges from 0 to 10"
                            )

                        if not form.errors:
                            # Calculate the total price
                            duration = (check_out_date - check_in_date).days
                            total_price = booking.cabin.price * duration

                            total_price += (
                                cave_exploration_tickets or
                                0) * Amenity.objects.get(
                                name='Cave Exploration').price
                            total_price += (
                                kayak_rentals or
                                0) * Amenity.objects.get(
                                name='Kayak Rental').price

                            booking.total_price = total_price
                            booking.save()

                            messages.success(
                                request,
                                "Booking updated successfully."
                            )
                            return redirect('booking_overview')
        else:
            # Handle form validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    if field != '__all__':
                        messages.warning(
                            request,
                            f"{form[field].label}: {error}"
                        )
    else:
        form = BookingForm(instance=booking, initial={
            'cave_exploration_tickets': booking.cave_exploration_tickets,
            'kayak_rentals': booking.kayak_rentals,
        })

    booked_dates = booked_dates.values_list('check_in_date', 'check_out_date')
    booked_dates_str = [[str(check_in_date), str(check_out_date)] for
                        check_in_date, check_out_date in booked_dates]

    context = {
        'form': form,
        'booking': booking,
        'booked_dates': booked_dates,
        'booked_dates_json': json.dumps(booked_dates_str),
    }

    return render(request, 'edit_booking.html', context)


@login_required
def delete_booking(request, booking_id):
    """
    This function handles the deletion of a booking identified by the
    provided booking_id. It retrieves the booking object associated with
    the provided ID and performs the deletion when a POST request is received.
    After successful deletion, it displays a success message and redirects
    the user to the booking overview page. Otherwise, it renders the
    'delete_booking.html' template, passing the booking object as context.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        # Perform booking deletion
        booking.delete()
        messages.success(request, "Booking deleted successfully.")
        return redirect('booking_overview')

    return render(request, 'delete_booking.html', {'booking': booking})


def custom_handler404(request, exception):
    """
    Custom handler for 404 (Page Not Found) errors.
    """
    return render(request, '404.html', status=404)


def custom_handler500(request):
    """
    Custom handler for 500 (Internal Server Error) errors.
    """
    return render(request, '500.html', status=500)
