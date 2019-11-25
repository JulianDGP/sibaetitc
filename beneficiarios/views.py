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

class Documento_identidadView(LoginRequiredMixin, generic.ListView):
    model = Documento_identidad
    template_name = 'beneficiarios/documento_list.html'
    context_object_name = 'obj'
    login_url = 'generales:login'

class Documento_identidadNew(LoginRequiredMixin, generic.CreateView):
    model = Documento_identidad
    template_name = 'beneficiarios/documento_form.html'
    context_object_name = 'obj'
    form_class = DocumentoForm
    success_url = reverse_lazy('beneficiarios:documento_list')
    login_url = 'generales:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class Documento_identidadEdit(LoginRequiredMixin, generic.UpdateView):
    model = Documento_identidad
    template_name = 'beneficiarios/documento_form.html'
    context_object_name = 'obj'
    form_class = DocumentoForm
    success_url = reverse_lazy('beneficiarios:documento_list')
    login_url = 'generales:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class Documento_identidadDel(LoginRequiredMixin, generic.DeleteView):
    model = Documento_identidad
    template_name = 'beneficiarios/documento_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('beneficiarios:documento_list')