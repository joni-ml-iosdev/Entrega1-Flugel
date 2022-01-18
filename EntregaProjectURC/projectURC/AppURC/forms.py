from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
import datetime

from django.forms.forms import Form


class FormularioAsegurado(forms.Form):

    razonSocial = forms.CharField(required=True)
    cuit = forms.IntegerField()

class FormularioExportaciones(forms.Form):

    exportando = forms.BooleanField()
    paisDestino = forms.CharField(max_length=40)
    clientes = forms.IntegerField()

class FormularioSiniestros(forms.Form):

    fechaSiniestro=forms.DateField(initial=datetime.date.today) # ayuda a la carga de la fecha 
    reclamado=forms.BooleanField()
    montoImplicado=forms.IntegerField()
    detalle=forms.CharField(max_length=140)

class FormularioCoberturas(forms.Form):

    tipo = forms.CharField(max_length=20)
    numeroPoliza = forms.ModelChoiceField(queryset=poliza.objects.all(), 
                                          required=True, 
                                          help_text="Polizas vigentes")
    
    fechaContratacion = forms.DateField(initial=datetime.date.today)
    fechaVigencia = forms.DateTimeField(initial= datetime.date.today)
    detalle = forms.CharField(max_length=40)
    

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']