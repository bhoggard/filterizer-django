from django.shortcuts import render
from artcalendar.models import Event

def index(request):
    context = {
        'opening_soon': Event.opening_soon(),
        'open_now': Event.open_now(),
    }
    return render(request, 'artcalendar/index.html', context)