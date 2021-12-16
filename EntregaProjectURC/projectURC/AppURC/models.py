from django.db import models

# Create your models here.

class poliza(models.Model):
    
    companiaAseg = models.CharField(max_length=40)
    montoAsegurado = models.IntegerField()

class Asegurado(models.Model):

    razonSocial = models.CharField(max_length=20)
    cuit = models.IntegerField()

class export(models.Model):
              
    exportando = models.BooleanField()
    paisDestino = models.CharField(max_length=40)
    clientes = models.IntegerField()

class Convenio(models.Model):

    camara = models.CharField(max_length=40)
    actividad = models.CharField(max_length=40)

class Documentacion(models.Model):

    formulario = models.IntegerField()
    detalleCompradores = models.IntegerField()
