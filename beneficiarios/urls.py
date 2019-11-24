from django.urls import path
from .views import *

urlpatterns = [
    path('generos/', GeneroView.as_view(), name='genero_list'),
    path('', Beneficiario.as_view(),name='beneficiario'),
]
