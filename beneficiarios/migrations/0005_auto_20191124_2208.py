# Generated by Django 2.2.7 on 2019-11-25 03:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beneficiarios', '0004_auto_20191123_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beneficiario',
            old_name='creado',
            new_name='fc',
        ),
        migrations.RenameField(
            model_name='beneficiario',
            old_name='modificado',
            new_name='fm',
        ),
        migrations.RenameField(
            model_name='dependencia',
            old_name='creado',
            new_name='fc',
        ),
        migrations.RenameField(
            model_name='dependencia',
            old_name='modificado',
            new_name='fm',
        ),
        migrations.RenameField(
            model_name='documento_identidad',
            old_name='creado',
            new_name='fc',
        ),
        migrations.RenameField(
            model_name='documento_identidad',
            old_name='modificado',
            new_name='fm',
        ),
        migrations.RenameField(
            model_name='genero',
            old_name='creado',
            new_name='fc',
        ),
        migrations.RenameField(
            model_name='genero',
            old_name='modificado',
            new_name='fm',
        ),
        migrations.RenameField(
            model_name='tipo_beneficiario',
            old_name='creado',
            new_name='fc',
        ),
        migrations.RenameField(
            model_name='tipo_beneficiario',
            old_name='modificado',
            new_name='fm',
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='uc',
            field=models.ForeignKey(default=1, on_delete=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='um',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dependencia',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dependencia',
            name='uc',
            field=models.ForeignKey(default=1, on_delete=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dependencia',
            name='um',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documento_identidad',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='documento_identidad',
            name='uc',
            field=models.ForeignKey(default=1, on_delete=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documento_identidad',
            name='um',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genero',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='genero',
            name='uc',
            field=models.ForeignKey(default=1, on_delete=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genero',
            name='um',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tipo_beneficiario',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tipo_beneficiario',
            name='uc',
            field=models.ForeignKey(default=1, on_delete=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipo_beneficiario',
            name='um',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]