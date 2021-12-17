from django import forms

class FormularioAsegurado(forms.Form):

    razonSocial = forms.CharField(required=True)
    cuit = forms.IntegerField()

class FormularioExportaciones(forms.Form):

    exportando = forms.BooleanField()
    paisDestino = forms.CharField(max_length=40)
    clientes = forms.IntegerField()