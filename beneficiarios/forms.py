from django import forms
from django.db import *

from .models import *
from django.contrib.auth.models import User


########################################################################################################################
class GeneroForm( forms.ModelForm ):
    class Meta:
        model = Genero
        fields = ['nombre_genero', 'estado']
        labels = {'nombre_genero': "Nombre del género", "estado": "Estado"}
        widget = {'nombre_genero': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )


class DocumentoForm( forms.ModelForm ):
    class Meta:
        model = Documento_identidad
        fields = ['nombre_documento_identidad', 'estado']
        labels = {'nombre_documento_identidad': "Nombre del documento de identidad", "estado": "Estado"}
        widget = {'nombre_documento_identidad': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )


class Tipo_beneficiarioForm( forms.ModelForm ):
    class Meta:
        model = Tipo_beneficiario
        fields = ['nombre_tipo_beneficiario', 'estado']
        labels = {'nombre_tipo_beneficiario': "Nombre del tipo de beneficiario", "estado": "Estado"}
        widget = {'nombre_tipo_beneficiario': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )


class DependenciaForm( forms.ModelForm ):
    class Meta:
        model = Dependencia
        fields = ['nombre_dependencia', 'estado']
        labels = {'nombre_dependencia': "Nombre de la dependencia", "estado": "Estado"}
        widget = {'nombre_dependencia': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )

########################################################################################################################

class BeneficiarioForm( forms.ModelForm ):
    documento_identidad = forms.ModelChoiceField(
        queryset=Documento_identidad.objects.filter( estado=True )
            .order_by( 'nombre_documento_identidad' )
    )
    genero_beneficiario = forms.ModelChoiceField(
        queryset=Genero.objects.filter( estado=True )
            .order_by( 'nombre_genero' )
    )
    dependencia_beneficiario = forms.ModelChoiceField(
        queryset=Dependencia.objects.filter( estado=True )
            .order_by( 'nombre_dependencia' )
    )
    tipo_beneficiario = forms.ModelChoiceField(
        queryset=Tipo_beneficiario.objects.filter( estado=True )
            .order_by( 'nombre_tipo_beneficiario' )
    )

    class Meta:
        model = Beneficiario
        fields = ['id_rfid_beneficiario', 'documento_identidad', 'numero_documento_identidad_beneficiario',
                  'genero_beneficiario', 'dependencia_beneficiario', 'tipo_beneficiario', 'nombres_beneficiario',
                  'apellidos_beneficiario', 'email_beneficiario', 'fecha_nacimiento_beneficiario', 'foto_beneficiario',
                  'estado']
        labels = {'id_rfid_beneficiario': 'RFID', 'documento_identidad': 'Documento',
                  'numero_documento_identidad_beneficiario': 'Num. Doc',
                  'genero_beneficiario': 'Género', 'dependencia_beneficiario': 'Dependencia',
                  'tipo_beneficiario': 'Tipo', 'nombres_beneficiario': 'Nombres',
                  'apellidos_beneficiario': 'Apellidos', 'email_beneficiario': 'E-mail',
                  'fecha_nacimiento_beneficiario': 'Fecha Nacimiento', 'foto_beneficiario': 'Foto', 'estado': 'Estado'}
        widget = {'id_rfid_beneficiario': forms.TextInput,
                  'numero_documento_identidad_beneficiario': 'Num. Doc',
                  'nombres_beneficiario': forms.TextInput,
                  'apellidos_beneficiario': forms.TextInput, 'email_beneficiario': forms.EmailInput,
                  'fecha_nacimiento_beneficiario': forms.TextInput, 'fecha_nacimiento_beneficiario': forms.DateField,
                  'estado': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        for field in iter( self.fields ):
            self.fields[field].widget.attrs.update( {
                'class': 'form-control'
            } )
