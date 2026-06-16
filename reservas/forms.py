from django import forms
from .models import Reserva
from django.utils import timezone 

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["espacio", "fecha", "hora", "hora_fin"] # 👈 Incluimos hora_fin
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}), # 👈 Nuevo widget
            'espacio': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'espacio': 'Espacio Común',
            'fecha': 'Fecha de Reserva',
            'hora': 'Hora de Inicio',
            'hora_fin': 'Hora de Término',
        }

    def clean_fecha(self):
        fecha_reserva = self.cleaned_data.get('fecha')
        fecha_actual = timezone.localdate()

        if fecha_reserva < fecha_actual:
            raise forms.ValidationError("No puedes elegir una fecha que ya pasó.")
        
        return fecha_reserva

    def clean(self):
        cleaned_data = super().clean()
        espacio = cleaned_data.get('espacio')
        fecha = cleaned_data.get('fecha')
        inicio = cleaned_data.get('hora')
        fin = cleaned_data.get('hora_fin')

        if inicio and fin:
            # Validar que no pongan que termina antes de empezar
            if fin <= inicio:
                raise forms.ValidationError("La hora de término debe ser posterior a la hora de inicio.")

            # ALGORITMO ANTI-SOLAPAMIENTOS
            # Busca cruces: (Inicio_Existente < Fin_Nuevo) Y (Fin_Existente > Inicio_Nuevo)
            cruces = Reserva.objects.filter(
                espacio=espacio,
                fecha=fecha,
                hora__lt=fin,
                hora_fin__gt=inicio
            )

            # Si estamos editando, ignoramos esta misma reserva
            if self.instance and self.instance.pk:
                cruces = cruces.exclude(pk=self.instance.pk)

            if cruces.exists():
                raise forms.ValidationError("❌ Este espacio ya se encuentra ocupado o se cruza con otra reserva en ese horario.")

        return cleaned_data