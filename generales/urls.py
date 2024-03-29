from django.urls import include, path
from django.contrib.auth import views as auth_views
from .views import Home

urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('login/',
         auth_views.LoginView.as_view(template_name='generales/login.html'),
         name='login'
         ),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='generales/login.html'),
         name='logout'
         ),

]
