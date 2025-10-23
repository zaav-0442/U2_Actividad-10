from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:clave_emp>', views.ver_empleado, name = 'ver_empleado'),
    path('agregar/', views.agregar_empleado, name = 'agregar_empleado'),
    path('editar/<int:clave_emp>', views.editar_empleado, name = 'editar_empleado'),
    path('eliminar/<int:clave_emp>', views.eliminar_empleado, name = 'eliminar_empleado'),
]