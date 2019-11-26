# Generated by Django 2.2.7 on 2019-11-26 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habilitacion_servicio',
            options={'verbose_name': 'Habilitación Servicio', 'verbose_name_plural': 'Habilitación Servicios'},
        ),
        migrations.AlterField(
            model_name='habilitacion_servicio',
            name='fecha_habilitacion_servicio',
            field=models.DateField(default=datetime.datetime(2019, 11, 26, 13, 47, 22, 45866), help_text='Fecha en que se habilita prestar un servicio', verbose_name='Fecha habilitación servicio'),
        ),
        migrations.AlterField(
            model_name='habilitacion_servicio',
            name='habilitado_habilitacion_servicio',
            field=models.BooleanField(help_text='Activo si se presta el servicio', null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='hora_fin_servicio',
            field=models.TimeField(verbose_name='Hora fin'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='hora_inicio_servicio',
            field=models.TimeField(verbose_name='Hora inicio'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='nombre_servicio',
            field=models.CharField(max_length=45, unique=True, verbose_name='Nombre servicio'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='valor_servicio',
            field=models.PositiveIntegerField(verbose_name='Valor servicio'),
        ),
    ]