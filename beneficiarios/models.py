from django.db import models
import os
# Create your models here.
from generales.models import Modelo


########################################################################################################################
class Genero( Modelo ):
    id_genero = models.AutoField(
        primary_key=True
    )

    nombre_genero = models.CharField(
        max_length=45,
        help_text='Nombre del género',
        unique=True,
        verbose_name='Nombre género'
    )

    def __str__(self):
        return '{}'.format( self.nombre_genero )

    def save(self):
        self.nombre_genero = self.nombre_genero.upper()
        super( Genero, self ).save()

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'

########################################################################################################################

class Documento_identidad( Modelo ):
    id_documento_identidad = models.AutoField(
        primary_key=True
    )

    nombre_documento_identidad = models.CharField(
        max_length=45,
        help_text='Nombre del documento de identidad',
        unique=True,
        verbose_name='Nombre documento'
    )

    def save(self):
        self.nombre_documento_identidad = self.nombre_documento_identidad.upper()
        super( Documento_identidad, self ).save()

    def __str__(self):
        return self.nombre_documento_identidad

    class Meta:
        verbose_name = 'Documento de identidad'
        verbose_name_plural = 'Documentos de identidad'


########################################################################################################################
class Tipo_beneficiario( Modelo ):
    id_tipo_beneficiario = models.AutoField(
        primary_key=True
    )

    nombre_tipo_beneficiario = models.CharField(
        max_length=45,
        help_text='Nombre del tipo de beneficiario, ej: Estudiante Bachillerato',
        unique=True,
        verbose_name='nombre tipo beneficiario'
    )

    def save(self):
        self.nombre_tipo_beneficiario = self.nombre_tipo_beneficiario.upper()
        super( Tipo_beneficiario, self ).save()

    def __str__(self):
        return self.nombre_tipo_beneficiario

    class Meta:
        verbose_name = 'Tipo de beneficiario'
        verbose_name_plural = 'Tipos de beneficiarios'


########################################################################################################################
class Dependencia( Modelo ):
    id_dependencia = models.AutoField(
        primary_key=True
    )

    nombre_dependencia = models.CharField(
        max_length=45,
        help_text='Nombre de la dependencia a la que pertenece, ej: Sistemas, Vigilancia',
        unique=True,
        verbose_name='Nombre dependencia'
    )

    def save(self):
        self.nombre_dependencia = self.nombre_dependencia.upper()
        super( Dependencia, self ).save()

    def __str__(self):
        return self.nombre_dependencia

    class Meta:
        verbose_name = 'Dependencia'
        verbose_name_plural = 'Dependencias'
########################################################################################################################

class Beneficiario( Modelo ):
    id_beneficiario = models.AutoField(
        primary_key=True
    )

    id_rfid_beneficiario = models.CharField(
        max_length=45,
        help_text='Id RFID carné o llavero    ',
        unique=True,
        verbose_name='Id RFID'
    )

    documento_identidad = models.ForeignKey(
        Documento_identidad,
        help_text='Documento de identidad del beneficiario',
        verbose_name='Documento de identidad',
        on_delete=False
    )

    numero_documento_identidad_beneficiario = models.CharField(
        max_length=15,
        help_text='Número del documento de identidad del beneficiario',
        unique=True,
        verbose_name='Número de documento'
    )

    genero_beneficiario = models.ForeignKey(
        Genero,
        help_text='Gérero del beneficiario',
        verbose_name='Género',
        on_delete=False
    )

    dependencia_beneficiario = models.ForeignKey(
        Dependencia,
        help_text='Dependencia a la que pertenece',
        verbose_name='Dependencia',
        on_delete=False
    )

    tipo_beneficiario = models.ForeignKey(
        Tipo_beneficiario,
        help_text='Tipo de beneficiario',
        verbose_name='Tipo beneficiario',
        on_delete=False
    )

    nombres_beneficiario = models.CharField(
        max_length=45,
        #help_text='Nombres del beneficiario',
        verbose_name='Nombres'
    )

    apellidos_beneficiario = models.CharField(
        max_length=45,
        #help_text='Apellidos del beneficiario',
        verbose_name='Apellidos'
    )

    email_beneficiario = models.EmailField(
        max_length=70,
        #help_text='Correo electrónico del beneficiario',
        verbose_name='Correo electrónico',
        unique=True
    )

    fecha_nacimiento_beneficiario = models.DateField(
        help_text='<em>AAAA-MM-DD</em>',
        verbose_name='Fecha de nacimiento'
    )

    saldo_beneficiario = models.IntegerField(
        verbose_name='Saldo',
        default=0,
        editable=False
    )

    foto_beneficiario = models.ImageField(
        upload_to='beneficiarios'
    )

    def save(self):
        self.id_rfid_beneficiario = self.id_rfid_beneficiario.upper()
        self.nombres_beneficiario = self.nombres_beneficiario.upper()
        self.apellidos_beneficiario = self.apellidos_beneficiario.upper()
        self.foto_beneficiario.name = '{}_{}.jpg'.format( self.id_beneficiario, self.fm )
        super( Beneficiario, self ).save()

    def __str__(self):
        return '{} {}'.format( self.apellidos_beneficiario, self.nombres_beneficiario )

    class Meta:
        verbose_name = 'Beneficiario'
        verbose_name_plural = 'Beneficiarios'
