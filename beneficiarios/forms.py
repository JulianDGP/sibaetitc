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

