"""sibaetitc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('', include(('generales.urls','generales'), namespace='generales')),
    path('beneficiarios/', include(('beneficiarios.urls','beneficiarios'), namespace='beneficiarios')),


    path('admin/', admin.site.urls),
]


'''path('servicios/', include(('servicios.urls','servicios'), namespace='servicios')),
    path('inscripciones/', include(('inscripciones.urls','inscripciones'), namespace='inscripciones')),
    path('recargas/', include(('recargas.urls','recargas'), namespace='recargas')),
    path('despachos/', include(('despachos.urls','despachos'), namespace='despachos')),
    path('sanciones/', include(('sanciones.urls','sanciones'), namespace='sanciones')),'''
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

