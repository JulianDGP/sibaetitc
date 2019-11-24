from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Genero



class Beneficiario(LoginRequiredMixin, generic.TemplateView):
    template_name = 'beneficiarios/beneficiarios.html'
    login_url = 'generales:login'

class GeneroView(LoginRequiredMixin, generic.ListView):
    model = Genero
    template_name = 'beneficiarios/genero_list.html'
    context_object_name = 'obj'
    login_url = 'generales:login'