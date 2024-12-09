from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['nombre', 'email', 'telefono', 'fecha_cita', 'hora_cita', 'mensaje']
        widgets = {
            'fecha_cita': forms.DateInput(attrs={'type': 'date'}),
            'hora_cita': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'nombre': 'Nombre completo',
            'email': 'Correo electrónico',
            'telefono': 'Teléfono (opcional)',
            'fecha_cita': 'Fecha de la cita',
            'hora_cita': 'Hora de la cita',
            'mensaje': 'Mensaje (opcional)',
        }
