from django.shortcuts import render


# Create your views here.
def get_sweet_spot(request):
    return render(request, 'sweet_spot/sweet_spot.html')
