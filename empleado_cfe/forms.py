from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre_emp', 'apellido_emp', 'puesto_emp', 'fecha_contratacion', 'activo_emp']
        labels = {
            'nombre_emp': 'Nombre del Empleado',
            'apellido_emp': 'Apellido del Empleado',
            'puesto_emp': 'Puesto del Empleado',
            'fecha_contratacion': 'Fecha de Contratación',
            'activo_emp': '¿Empleado Activo?',
        }
        widgets = {
            'nombre_emp': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_emp': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto_emp': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'}),
            'activo_emp': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }