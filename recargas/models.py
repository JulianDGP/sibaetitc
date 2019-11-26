from django.db import models
import os
# Create your models here.
from generales.models import Modelo
from beneficiarios.models import Beneficiario


class Recarga( Modelo ):
    id_recarga = models.AutoField(
        primary_key=True
    )

    beneficiario_recarga_saldo = models.ForeignKey(
        Beneficiario,
        help_text='Nombre del beneficiario',
        verbose_name='Nombre beneficiario',
        on_delete=False
    )

    valor_recarga = models.PositiveIntegerField(
        help_text='Valor recargado',
        verbose_name='Valor recarga'
    )

    def __str__(self):
        return '{}'.format( self.beneficiario_recarga_saldo)

    def save(self):
        self.nombre_genero = self.beneficiario_recarga_saldo.upper()
        super( Recarga, self ).save()

    class Meta:
        verbose_name = 'Recarga'
        verbose_name_plural = 'Recargas'

