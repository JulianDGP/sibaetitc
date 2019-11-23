from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse


class Beneficiario(generic.TemplateView):
    template_name = 'beneficiarios/beneficiarios.html'

