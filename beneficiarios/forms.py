from django import forms

from .models import *


class GeneroForm(forms.ModelForm):
    class Meta:
        model=Genero
        fields = ['nombre_genero','estado']
        labels = {'nombre_genero':"Nombre del género","estado":"Estado"}
        widget={'nombre_genero': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class DocumentoForm(forms.ModelForm):
    class Meta:
        model=Documento_identidad
        fields = ['nombre_documento_identidad','estado']
        labels = {'nombre_documento_identidad':"Nombre del documento de identidad","estado":"Estado"}
        widget={'nombre_documento_identidad': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class Tipo_beneficiarioForm(forms.ModelForm):
    class Meta:
        model=Tipo_beneficiario
        fields = ['nombre_tipo_beneficiario','estado']
        labels = {'nombre_tipo_beneficiario':"Nombre del tipo de beneficiario","estado":"Estado"}
        widget={'nombre_tipo_beneficiario': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })


class DependenciaForm(forms.ModelForm):
    class Meta:
        model=Dependencia
        fields = ['nombre_dependencia','estado']
        labels = {'nombre_dependencia':"Nombre de la dependencia","estado":"Estado"}
        widget={'nombre_dependencia': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })