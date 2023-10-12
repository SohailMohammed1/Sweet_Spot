from django.shortcuts import render, redirect
from .models import DinnerReservation
from .forms import ReservationForm

def get_sweet_spot(request):
    reservations = DinnerReservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'sweet_spot/sweet_spot.html', context)

def add_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.status = 0  # Set your desired default value for status
            reservation.save()
            return redirect('sweet_spot')
    else:
        form = ReservationForm()
    context = {
        'form': form,
        'reservations': DinnerReservation.objects.all()
    }
    return render(request, 'sweet_spot/add_reservation.html', context)


