from django.urls import path
from .views import *

urlpatterns = [
    path('generos/', GeneroView.as_view(), name='genero_list'),
    path('generos/new/', GeneroNew.as_view(), name='genero_new'),
    path('generos/edit/<int:pk>', GeneroEdit.as_view(), name='genero_edit'),
    path('generos/delete/<int:pk>', GeneroDel.as_view(), name='genero_del'),

]
