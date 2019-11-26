from django import forms
from django.db import *
from datetime import datetime

from .models import *
from django.contrib.auth.models import User


class ServicioForm( forms.ModelForm ):
    class Meta:
        model = Servicio
        fields = ['nombre_servicio', 'hora_inicio_servicio', 'hora_fin_servicio', 'valor_servicio', 'servicio_lunes',
                  'servicio_martes', 'servicio_miercoles', 'servicio_jueves', 'servicio_viernes', 'servicio_sabado', 'estado']
        labels = {'nombre_servicio':'Nombre del servicio', 'hora_inicio_servicio':'Hora inicio',
                  'hora_fin_servicio':'Hora finalización', 'valor_servicio':'Valor del servicio',
                  'servicio_lunes':'Lunes','servicio_martes':'Martes', 'servicio_miercoles':'Miércoles',
                  'servicio_jueves':'Jueves', 'servicio_viernes':'Viernes', 'servicio_sabado':'Sábado', 'estado':'Estado'}
        widget = {'nombre_servicio':forms.TextInput, 'hora_inicio_servicio':forms.TimeInput,
                  'hora_fin_servicio':forms.TimeInput, 'valor_servicio':forms.IntegerField,
                  'servicio_lunes':forms.CheckboxInput,'servicio_martes':forms.CheckboxInput, 'servicio_miercoles':forms.CheckboxInput,
                  'servicio_jueves':forms.CheckboxInput, 'servicio_viernes':forms.CheckboxInput, 'servicio_sabado':forms.CheckboxInput, 'estado':forms.CheckboxInput}

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )

class Habilitacion_servicioForm( forms.ModelForm ):
    servicio_habilitacion_servicio = forms.ModelChoiceField(
        queryset=Servicio.objects.filter( estado=True )
            .order_by( 'nombre_servicio' )
    )
    class Meta:
        model = Habilitacion_servicio
        fields = ['servicio_habilitacion_servicio', 'fecha_habilitacion_servicio', 'estado']
        labels = {}
        widget = {}



    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )

    def clean_fecha_habilitacion_servicio(self):
        fecha_habilitacion_servicio = self.cleaned_data['fecha_habilitacion_servicio']
        print( datetime.now().day )
        if fecha_habilitacion_servicio is datetime.now():
            self.add_error( 'fecha_habilitacion_servicio', 'La fecha no puede ser la de hoy' )
        else:
            return self.cleaned_data['fecha_habilitacion_servicio']