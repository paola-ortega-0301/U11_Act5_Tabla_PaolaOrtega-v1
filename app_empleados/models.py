from django.db import models

# Create your models here.
class Empleados(models.Model):
    nombre = models.CharField(max_length=100)
    # CORRECCIÓN: Usar CharField para el teléfono y especificar max_length
    # Los números de teléfono pueden tener guiones, paréntesis, espacios, etc.
    telefono = models.CharField(max_length=20, null=True, blank=True) # Añadí null=True, blank=True para hacerlo opcional
    correo = models.EmailField(unique=True)

    # CORRECCIÓN: El método debe llamarse __str__ (doble guion bajo)
    def __str__(self):
        return f"{self.nombre} ({self.telefono})" # Ahora usa el campo teléfono correctamente

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"