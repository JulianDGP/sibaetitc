from django.db import models

# Create your models here.
class Modelo(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
