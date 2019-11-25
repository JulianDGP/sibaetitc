from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Modelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True, editable=False)
    fm = models.DateTimeField(auto_now=True, editable=False)
    uc = models.ForeignKey(User, on_delete=False, editable=False)
    um = models.IntegerField(blank=True, null=True, editable=False)

    class Meta:
        abstract = True
