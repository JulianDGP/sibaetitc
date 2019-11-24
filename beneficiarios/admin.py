from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre_genero',)

@admin.register(Documento_identidad)
class Documento_identidadAdmin(admin.ModelAdmin):
    list_display = ('nombre_documento_identidad',)

@admin.register(Tipo_beneficiario)
class Tipo_beneficiarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_tipo_beneficiario',)

@admin.register(Dependencia)
class DependenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre_dependencia',)

@admin.register(Beneficiario)
class BeneficiarioAdmin(admin.ModelAdmin):
    list_display = ('id_rfid_beneficiario', 'documento_identidad', 'numero_documento_identidad_beneficiario', 'nombres_beneficiario',
                    'apellidos_beneficiario', 'email_beneficiario', 'fecha_nacimiento_beneficiario', 'saldo_beneficiario', 'genero_beneficiario',
                    'tipo_beneficiario', 'dependencia_beneficiario', 'foto_beneficiario')