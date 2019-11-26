from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


from .models import *
from .forms import *

########################################################################################################################

class ServicioView(LoginRequiredMixin, generic.ListView):
    model = Servicio
    template_name = 'servicios/servicio_list.html'
    context_object_name = 'obj'
    login_url = 'generales:login'

class ServicioNew(LoginRequiredMixin, generic.CreateView):
    model = Servicio
    template_name = 'servicios/servicio_form.html'
    context_object_name = 'obj'
    form_class = ServicioForm
    success_url = reverse_lazy('servicios:servicio_list')
    login_url = 'generales:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ServicioEdit(LoginRequiredMixin, generic.UpdateView):
    model = Servicio
    template_name = 'servicios/servicio_form.html'
    context_object_name = 'obj'
    form_class = ServicioForm
    success_url = reverse_lazy('servicios:servicio_list')
    login_url = 'generales:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ServicioDel(LoginRequiredMixin, generic.DeleteView):
    model = Servicio
    template_name = 'servicios/servicio_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('servicios:servicio_list')


########################################################################################################################


class Habilitacion_servicioView(LoginRequiredMixin, generic.ListView):
    model = Habilitacion_servicio
    template_name = 'servicios/habilitacion_servicio_list.html'
    context_object_name = 'obj'
    login_url = 'generales:login'

class Habilitacion_servicioNew(LoginRequiredMixin, generic.CreateView):
    model = Habilitacion_servicio
    template_name = 'servicios/habilitacion_servicio_form.html'
    context_object_name = 'obj'
    form_class = Habilitacion_servicioForm
    success_url = reverse_lazy('servicios:habilitacion_servicio_list')
    login_url = 'generales:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class Habilitacion_servicioEdit(LoginRequiredMixin, generic.UpdateView):
    model = Habilitacion_servicio
    template_name = 'servicios/habilitacion_servicio_form.html'
    context_object_name = 'obj'
    form_class = Habilitacion_servicioForm
    success_url = reverse_lazy('servicios:habilitacion_servicio_list')
    login_url = 'generales:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class Habilitacion_servicioDel(LoginRequiredMixin, generic.DeleteView):
    model = Habilitacion_servicio
    template_name = 'servicios/habilitacion_servicio_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('servicios:habilitacion_servicio_list')