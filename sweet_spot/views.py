from django.shortcuts import render, redirect
from .models import DinnerReservation


def get_sweet_spot(request):
    reservations = DinnerReservation.objects.all()

    context = {
        'reservations': reservations
    }

    return render(request, 'sweet_spot/sweet_spot.html', context)

def add_reservation(request):
    if request.method == "POST":
        # Extract form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        no_of_guests = request.POST.get('no_of_guests')
        date_selected = request.POST.get('date_selected')
        time_selected = request.POST.get('time_selected')
        special_request = request.POST.get('special_request')

        # Check if a reservation with the same first_name already exists
        existing_reservation = DinnerReservation.objects.filter(first_name=first_name).first()

        if existing_reservation:
            # Update the existing reservation
            existing_reservation.last_name = last_name
            existing_reservation.email = email
            existing_reservation.phone_number = phone_number
            existing_reservation.no_of_guests = no_of_guests
            existing_reservation.date_selected = date_selected
            existing_reservation.time_selected = time_selected
            existing_reservation.special_request = special_request
            existing_reservation.save()
        else:
            # Create a new DinnerReservation object
            DinnerReservation.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                no_of_guests=no_of_guests,
                date_selected=date_selected,
                time_selected=time_selected,
                special_request=special_request,
                status=0  # Assuming 0 represents the initial status of the reservation
            )

        # Redirect to a success page or any other appropriate action
        return redirect('sweet_spot')  # Redirect to the view where you display reservations (assuming it's named 'sweet_spot')

    return render(request, 'sweet_spot/add_reservation.html')


