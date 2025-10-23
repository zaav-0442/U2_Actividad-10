from django.db import models

# Create your models here.
class Empleado(models.Model):
    clave_emp = models.AutoField(
        primary_key=True,
        unique=True,
        verbose_name="Clave de Empleado"
    )
    nombre_emp = models.CharField(
        max_length=100,
        verbose_name="Nombre"
    )
    apellido_emp = models.CharField(
        max_length=100,
        verbose_name="Apellido"
    )
    puesto_emp = models.CharField(
        max_length=100,
        verbose_name="Puesto"
    )
    fecha_contratacion = models.DateField(
        verbose_name="Fecha de Contratación"
    )
    activo_emp = models.BooleanField(
        default=True,
        verbose_name="Activo"
    )

    class Meta:
        db_table = 'Empleado' 
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f"Empleado: {self.nombre_emp} {self.apellido_emp} ({self.clave_emp})"