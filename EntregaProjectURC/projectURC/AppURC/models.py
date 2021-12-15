from django.db import models

# Create your models here.

class poliza(models.Model):
    
    empresa = models.CharField(max_length=40)
    montoAsegurado = models.IntegerField()

class Asegurado(models.Model):

    razonSocial = models.CharField(max_length=20)
    cuit = models.IntegerField()
    mailContact = models.EmailField()
    inicioCobertura = models.DateField() 

class export(models.Model):

                            
    exportando = models.BooleanField()
    paisDestino = models.CharField(max_length=40)
    clientes = models.IntegerField()