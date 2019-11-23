from django.urls import path
from .views import *

urlpatterns = [
    path('', Beneficiario.as_view(),name='beneficiario'),
]
