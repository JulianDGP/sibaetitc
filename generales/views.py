from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse


class HomePage(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Página de inicio')

class Home(generic.TemplateView):
    template_name = 'generales/home.html'

