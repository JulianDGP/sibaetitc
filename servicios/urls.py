from django.urls import path
from .views import *

urlpatterns = [
    path('servicios/', ServicioView.as_view(), name='servicio_list'),
    path('servicios/new/', ServicioNew.as_view(), name='servicio_new'),
    path('servicios/edit/<int:pk>', ServicioEdit.as_view(), name='servicio_edit'),
    path('servicios/delete/<int:pk>', ServicioDel.as_view(), name='servicio_del'),

    path('habilitacion_servicios/', Habilitacion_servicioView.as_view(), name='habilitacion_servicio_list'),
    path('habilitacion_servicios/new/', Habilitacion_servicioNew.as_view(), name='habilitacion_servicio_new'),
    path('habilitacion_servicios/edit/<int:pk>', Habilitacion_servicioEdit.as_view(), name='habilitacion_servicio_edit'),
    path('habilitacion_servicios/delete/<int:pk>', Habilitacion_servicioDel.as_view(), name='habilitacion_servicio_del'),
]
