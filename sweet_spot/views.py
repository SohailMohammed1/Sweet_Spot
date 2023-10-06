from django.shortcuts import render
from .models import DinnerReservation  

def get_sweet_spot(request):
    reservations = DinnerReservation.objects.all()

    
    context = {
        'reservations': reservations
    }

    
    return render(request, 'sweet_spot/sweet_spot.html', context)
