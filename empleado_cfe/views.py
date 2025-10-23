from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.
def index(request):
    return render(request, 'empleado_cfe/index.html', {
        'empleados': Empleado.objects.all()
    })

def ver_empleado(request, clave_emp):
    empleado = Empleado.objects.get(PK = clave_emp)
    return HttpResponseRedirect(reverse('index'))

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            nuevo_nombre = form.cleaned_data['nombre_emp']
            nuevo_apellido = form.cleaned_data['apellido_emp']
            nuevo_puesto = form.cleaned_data['puesto_emp']
            nueva_fecha_contratacion = form.cleaned_data['fecha_contratacion']
            nuevo_activo = form.cleaned_data['activo_emp']

            nuevo_empleado = Empleado(
                nombre_emp = nuevo_nombre,
                apellido_emp = nuevo_apellido,
                puesto_emp = nuevo_puesto,
                fecha_contratacion = nueva_fecha_contratacion,
                activo_emp = nuevo_activo
            )

            nuevo_empleado.save()

            return render(request, 'empleado_cfe/agregar_empleado.html', {
                'form' : EmpleadoForm(),
                'success' : True 
            })
    else:
        form = EmpleadoForm()
    return render(request, 'empleado_cfe/agregar_empleado.html', {
        'form' : EmpleadoForm()
    })

def editar_empleado(request, clave_emp):
    try:
        empleado = Empleado.objects.get(clave_emp = clave_emp)
    except Empleado.DoesNotExist:
        messages.error(request, "El empleado solicitado no existe.")
        return redirect('index')
    
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance = empleado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado actualizado exitosamente.')
            return redirect('index')
    else :
        form = EmpleadoForm(instance = empleado)
    return render(request, 'empleado_cfe/editar_empleado.html', {
        'form': form,
        'empleado': empleado 
    })

def eliminar_empleado(request, clave_emp):
    if request.method == 'POST': 
        try:
            empleado = Empleado.objects.get(pk=clave_emp) 
            messages.success(request, f'Empleado {empleado.nombre_emp} eliminado exitosamente.')
            
            empleado.delete()
        
        except Empleado.DoesNotExist:
            messages.error(request, 'Error: El empleado que intentas eliminar no existe.')

    return HttpResponseRedirect(reverse('index'))