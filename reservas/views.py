from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Reserva
from .forms import ReservaForm
from django.http import JsonResponse


@login_required
def index(request):
    if request.user.is_superuser:
        reservas = Reserva.objects.all().order_by("-id")
    else:
        reservas = Reserva.objects.filter(usuario=request.user).order_by("-id")
    return render(request, "reservas/index.html", {"reservas": reservas})

@login_required
def crear(request):
    fecha_sugerida = request.GET.get('fecha')
    hoy = timezone.localdate()

    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            messages.success(request, "¡Reserva creada con éxito!")
            return redirect('reservas:index')
    else:
        if fecha_sugerida:
            form = ReservaForm(initial={'fecha': fecha_sugerida})
        else:
            form = ReservaForm()
            
    # 👈 NUEVO: Traemos las reservas de hoy para mostrarlas como "Horarios ocupados"
    reservas_hoy = Reserva.objects.filter(fecha=hoy).order_by('hora')

    return render(request, 'reservas/crear.html', {
        'form': form,
        'reservas_hoy': reservas_hoy # 👈 Lo pasamos al template
    })
@login_required
def agenda(request):
    agendas = Reserva.objects.all().order_by('fecha', 'hora')
    
    return render(request, 'reservas/agenda.html', {
        'agendas': agendas,
        'hoy': timezone.now().date()  
    })

@login_required
def editar_reserva(request, id):
    try:
        if request.user.is_superuser:
            reserva = Reserva.objects.get(id=id)
        else:
            reserva = Reserva.objects.get(id=id, usuario=request.user)
    except Reserva.DoesNotExist:
        messages.error(request, "La reserva no existe o no tienes permiso.")
        return redirect('reservas:index')

    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            messages.success(request, "Reserva actualizada.")
            return redirect('reservas:index')
    else:
        form = ReservaForm(instance=reserva)
    
    return render(request, 'reservas/editar.html', {'form': form, 'reserva': reserva})

@login_required
def eliminar_reserva(request, id):
    try:
        if request.user.is_superuser:
            reserva = Reserva.objects.get(id=id)
        else:
            reserva = Reserva.objects.get(id=id, usuario=request.user)
    except Reserva.DoesNotExist:
        return redirect('reservas:index')
    
    if request.method == "POST":
        reserva.delete()
        messages.success(request, "Reserva eliminada correctamente.")
        return redirect('reservas:index')
    
    return render(request, 'reservas/eliminar_confirmar.html', {'reserva': reserva})

def api_eventos(request):
    # Traemos todas las reservas de la base de datos usando tu método común
    reservas = Reserva.objects.all()
    lista_eventos = []
    
    # Recorremos las reservas y las guardamos en un formato que el calendario entiende
    for r in reservas:
        lista_eventos.append({
            'title': f"{r.espacio.nombre} ({r.usuario.username})",
            'start': f"{r.fecha}T{r.hora}",      # Formato obligatorio: Año-Mes-DíaTHora
            'end': f"{r.fecha}T{r.hora_fin}",   
            'color': '#0d6efd' if 'cowork' in r.espacio.nombre.lower() else '#198754'
        })
        
    # Devolvemos la lista limpia
    return JsonResponse(lista_eventos, safe=False)