from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
    numeroPoliza = forms.IntegerField()
    fechaContratacion = forms.DateField(initial=datetime.date.today)
    fechaVigencia = forms.DateTimeField(initial= datetime.date.today)
    detalle = forms.CharField(max_length=40)