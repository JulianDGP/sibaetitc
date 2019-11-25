from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


from .models import *
from .forms import *



class GeneroView(LoginRequiredMixin, generic.ListView):
    model = Genero
    template_name = 'beneficiarios/genero_list.html'
    context_object_name = 'obj'
    login_url = 'generales:login'

class GeneroNew(LoginRequiredMixin, generic.CreateView):
    model = Genero
    template_name = 'beneficiarios/genero_form.html'
    context_object_name = 'obj'
    form_class = GeneroForm
    success_url = reverse_lazy('beneficiarios:genero_list')
    login_url = 'generales:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class GeneroEdit(LoginRequiredMixin, generic.UpdateView):
    model = Genero
    template_name = 'beneficiarios/genero_form.html'
    context_object_name = 'obj'
    form_class = GeneroForm
    success_url = reverse_lazy('beneficiarios:genero_list')
    login_url = 'generales:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class GeneroDel(LoginRequiredMixin, generic.DeleteView):
    model = Genero
    template_name = 'beneficiarios/genero_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('beneficiarios:genero_list')