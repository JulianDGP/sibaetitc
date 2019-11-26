from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


from .models import *
from .forms import *

########################################################################################################################

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

########################################################################################################################

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
    success_url = reverse_lazy('beneficiarios:tipo_beneficiario_list')
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
    success_url = reverse_lazy('beneficiarios:tipo_beneficiario_list')



########################################################################################################################

class Tipo_beneficiarioView(LoginRequiredMixin, generic.ListView):
    model = Tipo_beneficiario
    template_name = 'beneficiarios/tipo_beneficiarios_list.html'
    context_object_name = 'obj'
    login_url = 'generales:login'

class Tipo_beneficiarioNew(LoginRequiredMixin, generic.CreateView):
    model = Tipo_beneficiario
    template_name = 'beneficiarios/tipo_beneficiario_form.html'
    context_object_name = 'obj'
    form_class = Tipo_beneficiarioForm
    success_url = reverse_lazy('beneficiarios:tipo_beneficiario_list')
    login_url = 'generales:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class Tipo_beneficiarioEdit(LoginRequiredMixin, generic.UpdateView):
    model = Tipo_beneficiario
    template_name = 'beneficiarios/tipo_beneficiario_form.html'
    context_object_name = 'obj'
    form_class = Tipo_beneficiarioForm
    success_url = reverse_lazy('beneficiarios:tipo_beneficiario_list')
    login_url = 'generales:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class Tipo_beneficiarioDel(LoginRequiredMixin, generic.DeleteView):
    model = Tipo_beneficiario
    template_name = 'beneficiarios/tipo_beneficiario_form.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('beneficiarios:tipo_beneficiario_list')


########################################################################################################################


class DependenciaView(LoginRequiredMixin, generic.ListView):
    model = Dependencia
    template_name = 'beneficiarios/dependencia_list.html'
    context_object_name = 'obj'
    login_url = 'generales:login'

class DependenciaNew(LoginRequiredMixin, generic.CreateView):
    model = Dependencia
    template_name = 'beneficiarios/dependencia_form.html'
    context_object_name = 'obj'
    form_class = DependenciaForm
    success_url = reverse_lazy('beneficiarios:dependencia_list')
    login_url = 'generales:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class DependenciaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Dependencia
    template_name = 'beneficiarios/dependencia_form.html'
    context_object_name = 'obj'
    form_class = DependenciaForm
    success_url = reverse_lazy('beneficiarios:dependencia_list')
    login_url = 'generales:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class DependenciaDel(LoginRequiredMixin, generic.DeleteView):
    model = Dependencia
    template_name = 'beneficiarios/dependencia_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('beneficiarios:dependencia_list')




########################################################################################################################


class BeneficiarioView(LoginRequiredMixin, generic.ListView):
    model = Beneficiario
    template_name = 'beneficiarios/beneficiario_list.html'
    context_object_name = 'obj'
    login_url = 'generales:login'

class BeneficiarioNew(LoginRequiredMixin, generic.CreateView):
    model = Beneficiario
    template_name = 'beneficiarios/beneficiario_form.html'
    context_object_name = 'obj'
    form_class = BeneficiarioForm
    success_url = reverse_lazy('beneficiarios:beneficiario_list')
    login_url = 'generales:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class BeneficiarioEdit(LoginRequiredMixin, generic.UpdateView):
    model = Beneficiario
    template_name = 'beneficiarios/beneficiario_form.html'
    context_object_name = 'obj'
    form_class = BeneficiarioForm
    success_url = reverse_lazy('beneficiarios:beneficiario_list')
    login_url = 'generales:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class BeneficiarioDel(LoginRequiredMixin, generic.DeleteView):
    model = Beneficiario
    template_name = 'beneficiarios/beneficiario_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('beneficiarios:beneficiario_list')