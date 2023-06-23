from django.contrib import admin
from .models import DinnerReservation
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(DinnerReservation)
