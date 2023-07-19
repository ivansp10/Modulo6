from django.contrib import admin
from .models import Vehiculo

# Register your models here.
class VehiculoAdmin(admin.ModelAdmin):
    readonly_fields=('fecha_creacion','fecha_modificacion')

admin.site.register(Vehiculo,VehiculoAdmin)