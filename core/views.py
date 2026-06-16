from django.shortcuts import render, redirect
from django.utils import timezone
from reservas.models import Reserva 
from .forms import ContactoForm
from .models import ContactoMensaje

def home(request):
    hoy = timezone.localdate()
    total_hoy = Reserva.objects.filter(fecha=hoy).count()
    return render(request, 'core/home.html', {'total_hoy': total_hoy})

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            print("--- ¡EL FORMULARIO ES VÁLIDO! Guardando... ---")
            form.save() 
            return redirect('core:home')
        else:
            print("--- ¡EL FORMULARIO TIENE ERRORES! ---")
            print(form.errors) 
    else:
        form = ContactoForm()
        
    return render(request, 'core/contacto.html', {'form': form})

def panel_mensajes(request):
    if request.user.is_authenticated and request.user.is_staff:
        mensajes = ContactoMensaje.objects.all()
        return render(request, 'core/panel_mensajes.html', {'mensajes': mensajes})
    else:
        return redirect('core:home')