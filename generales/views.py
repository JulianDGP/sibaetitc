from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'generales/home.html'
    login_url = 'generales:login'