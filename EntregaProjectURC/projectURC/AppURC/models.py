from django.db import models

# Create your models here.

class poliza(models.Model): # con vista coberturas/template coberturas
    
    companiaAseg = models.CharField(max_length=40)
    montoAsegurado = models.IntegerField()

class Asegurado(models.Model): #con vista datosAsegurado/template ficha

    razonSocial = models.CharField(max_length=20)
    cuit = models.IntegerField()

class export(models.Model): #con vista exportaciones/template exportaciones
              
    exportando = models.BooleanField()
    paisDestino = models.CharField(max_length=40)
    clientes = models.IntegerField()

class Convenio(models.Model): #con vista convenio/template convenio

    camara = models.CharField(max_length=40)
    actividad = models.CharField(max_length=40)

class Documentacion(models.Model): #con vista documentacion

    formulario = models.IntegerField()
    detalleCompradores = models.IntegerField()
