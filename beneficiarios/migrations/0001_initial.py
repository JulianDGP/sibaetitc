# Generated by Django 2.2.7 on 2019-11-23 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('id_genero', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_genero', models.CharField(help_text='Nombre del género', max_length=50, unique=True, verbose_name='Nombre género')),
            ],
            options={
                'verbose_name': 'Género',
                'verbose_name_plural': 'Géneros',
            },
        ),
    ]
