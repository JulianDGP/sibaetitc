import os
# Create your models here.
from django.db import models
from generales.models import Modelo
from datetime import datetime


class Servicio( Modelo ):
    id_servicio = models.AutoField(
        primary_key=True
    )

    nombre_servicio = models.CharField(
        max_length=45,
        #help_text='Nombre del servicio',
        unique=True,
        verbose_name='Nombre servicio'
    )

    hora_inicio_servicio = models.TimeField(
        #help_text='Hora de inicio',
        verbose_name='Hora inicio'
    )

    hora_fin_servicio = models.TimeField(
        #help_text='Hora de fin',
        verbose_name='Hora fin'
    )

    valor_servicio = models.PositiveIntegerField(
        #help_text='Valor del servicio',
        verbose_name='Valor servicio'
    )

    servicio_lunes = models.BooleanField(
        help_text='El servicio se presta el lunes',
        verbose_name='Lunes',
        default=True
    )

    servicio_martes = models.BooleanField(
        help_text='El servicio se presta el martes',
        verbose_name='martes',
        default=True
    )

    servicio_miercoles = models.BooleanField(
        help_text='El servicio se presta el miércoles',
        verbose_name='Miercoles',
        default=True
    )

    servicio_jueves = models.BooleanField(
        help_text='El servicio se presta el jueves',
        verbose_name='Jueves',
        default=True
    )

    servicio_viernes = models.BooleanField(
        help_text='El servicio se presta el viernes',
        verbose_name='Viernes',
        default=True
    )

    servicio_sabado = models.BooleanField(
        help_text='El servicio se presta el sábado',
        verbose_name='Sábado',
        default=True
    )




    def __str__(self):
        return '{}'.format( self.nombre_servicio )

    def save(self):
        self.nombre_servicio = self.nombre_servicio.upper()
        super( Servicio, self ).save()

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
########################################################################################################################

class Habilitacion_servicio( Modelo ):
    id_habilitacion_servicio = models.AutoField(
        primary_key=True
    )

    servicio_habilitacion_servicio = models.ForeignKey(
        Servicio,
        help_text='Servicio a habilitar',
        verbose_name='Servicio a habilitar',
        on_delete=False
    )

    fecha_habilitacion_servicio = models.DateField(
        help_text='Fecha en que se habilita prestar un servicio',
        verbose_name='Fecha habilitación servicio',
        default=datetime.now()

    )

    habilitado_habilitacion_servicio = models.BooleanField(
        help_text='Activo si se presta el servicio',
        verbose_name='Estado'
    )

    def __str__(self):
        return '{} {}'.format( self.servicio_habilitacion_servicio,self.fecha_habilitacion_servicio)


    class Meta:
        verbose_name = 'Habilitación Servicio'
        verbose_name_plural = 'Habilitación Servicios'