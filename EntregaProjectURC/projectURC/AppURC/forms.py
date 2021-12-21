from django import forms
import datetime


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