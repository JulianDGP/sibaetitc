from django.urls import path
from .views import *

urlpatterns = [
    path('generos/', GeneroView.as_view(), name='genero_list'),
    path('generos/new/', GeneroNew.as_view(), name='genero_new'),
    path('generos/edit/<int:pk>', GeneroEdit.as_view(), name='genero_edit'),
    path('generos/delete/<int:pk>', GeneroDel.as_view(), name='genero_del'),

    path( 'documentos/', Documento_identidadView.as_view(), name='documento_list'),
    path( 'documentos/new/', Documento_identidadNew.as_view(), name='documento_new'),
    path( 'documentos/edit/<int:pk>', Documento_identidadEdit.as_view(), name='documento_edit'),
    path( 'documentos/delete/<int:pk>', Documento_identidadDel.as_view(), name='documento_del'),

    path( 'tipos_beneficiario/', Tipo_beneficiarioView.as_view(), name='tipo_beneficiario_list'),
    path( 'tipos_beneficiario/new/', Tipo_beneficiarioNew.as_view(), name='tipo_beneficiario_new'),
    path( 'tipos_beneficiario/edit/<int:pk>', Tipo_beneficiarioEdit.as_view(), name='tipo_beneficiario_edit'),
    path( 'tipos_beneficiario/delete/<int:pk>', Tipo_beneficiarioDel.as_view(), name='tipo_beneficiario_del'),

    path('dependencias/', DependenciaView.as_view(), name='dependencia_list'),
    path('dependencias/new/', DependenciaNew.as_view(), name='dependencia_new'),
    path('dependencias/edit/<int:pk>', DependenciaEdit.as_view(), name='dependencia_edit'),
    path('dependencias/delete/<int:pk>', DependenciaDel.as_view(), name='dependencia_del'),

    path('beneficiarios/', BeneficiarioView.as_view(), name='beneficiario_list'),
    path('beneficiarios/new/', BeneficiarioNew.as_view(), name='beneficiario_new'),
    path('beneficiarios/edit/<int:pk>', BeneficiarioEdit.as_view(), name='beneficiario_edit'),
    path('beneficiarios/delete/<int:pk>', BeneficiarioDel.as_view(), name='beneficiario_del'),
]
