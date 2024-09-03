from django.shortcuts import render

# Create your views here.
from .models import Servicio, Agenda
from datetime import datetime

def index(request):
    return render(request, 'index.html', {'current_time': datetime.now()})

def ubicacion(request):
    return render(request, 'ubicacion.html')

def agendar(request):
    return render(request, 'agendar.html')

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})

def login(request):
    return render(request, 'login.html')

def agenda(request):
    agenda_items = Agenda.objects.all()
    return render(request, 'agenda.html', {'agenda_items': agenda_items})