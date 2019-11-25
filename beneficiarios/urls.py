from django.urls import path
from .views import *

urlpatterns = [
    path('generos/', GeneroView.as_view(), name='genero_list'),
    path('generos/new/', GeneroNew.as_view(), name='genero_new'),
    path('generos/edit/<int:pk>', GeneroEdit.as_view(), name='genero_edit'),
    path('generos/delete/<int:pk>', GeneroDel.as_view(), name='genero_del'),

    path( 'documentos/', Documento_identidadView.as_view(), name='documento_list' ),
    path( 'documentos/new/', Documento_identidadNew.as_view(), name='documento_new' ),
    path( 'documentos/edit/<int:pk>', Documento_identidadEdit.as_view(), name='documento_edit' ),
    path( 'documentos/delete/<int:pk>', Documento_identidadDel.as_view(), name='documento_del' ),

]
