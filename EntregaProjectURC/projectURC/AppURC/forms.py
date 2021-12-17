from django import forms

class FormularioAsegurado(forms.Form):

    razonSocial = forms.CharField(required=True)
    cuit = forms.IntegerField()