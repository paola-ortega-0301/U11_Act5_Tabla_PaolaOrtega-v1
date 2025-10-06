from django.contrib import admin

# Register your models here.

from .models import Empleados
#Registrar el modelo Empleados en el admin
admin.site.register(Empleados)