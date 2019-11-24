# Generated by Django 2.2.7 on 2019-11-23 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('id_dependencia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_dependencia', models.CharField(help_text='Nombre de la dependencia a la que pertenece, ej: Sistemas, Vigilancia', max_length=50, unique=True, verbose_name='Nombre dependencia')),
            ],
            options={
                'verbose_name': 'Dependencia',
                'verbose_name_plural': 'Dependencias',
            },
        ),
        migrations.CreateModel(
            name='Documento_identidad',
            fields=[
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('id_documento_identidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_documento_identidad', models.CharField(help_text='Nombre del documento de identidad', max_length=50, unique=True, verbose_name='Nombre documento')),
            ],
            options={
                'verbose_name': 'Documento de identidad',
                'verbose_name_plural': 'Documentos de identidad',
            },
        ),
        migrations.CreateModel(
            name='Tipo_beneficiario',
            fields=[
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('id_tipo_beneficiario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_beneficiario', models.CharField(help_text='Nombre del tipo de beneficiario, ej: Estudiante Bachillerato', max_length=50, unique=True, verbose_name='nombre tipo beneficiario')),
            ],
            options={
                'verbose_name': 'Tipo de beneficiario',
                'verbose_name_plural': 'Tipos de beneficiarios',
            },
        ),
    ]
