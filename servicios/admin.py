from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id_servicio','nombre_servicio','hora_inicio_servicio','hora_fin_servicio','valor_servicio',
                    'servicio_lunes','servicio_martes','servicio_miercoles','servicio_jueves','servicio_viernes',
                    'servicio_sabado','estado','fc','fm','uc','um',)

@admin.register(Habilitacion_servicio)
class Habilitacion_servicioAdmin(admin.ModelAdmin):
    list_display = ('id_habilitacion_servicio', 'servicio_habilitacion_servicio', 'fecha_habilitacion_servicio', 'estado', 'fc', 'fm', 'uc', 'um')
