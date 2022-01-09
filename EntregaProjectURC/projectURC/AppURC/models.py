from django.db import models
from django.db.models.fields import DateField

# Create your models here.

class poliza(models.Model): # con vista coberturas/template coberturas
    cliente_id = models.OneToOneField("Cliente", null=True ,blank=True, on_delete=models.RESTRICT)
    poliza_id = models.AutoField(primary_key=True)
    companiaAseg = models.CharField(max_length=40)
    montoAsegurado = models.IntegerField()
    coberturas = models.ManyToManyField("Cobertura", null=True, blank=True)

    def __str__(self): # me sirve para ver en admin la info cargada

        return f"Compañía Aseguradora: {self.companiaAseg} | Monto Asegurado: {self.montoAsegurado}"

class Asegurado(models.Model): #con vista datosAsegurado/template ficha

    razonSocial = models.CharField(max_length=20)
    cuit = models.IntegerField()
    
    def __str__(self): # me sirve para ver en admin la info cargada

        return f"Empresa Asegurada: {self.razonSocial} | CUIT del Asegurado: {self.cuit}"

class export(models.Model): #con vista exportaciones/template exportaciones
              
    exportando = models.BooleanField()
    paisDestino = models.CharField(max_length=40)
    clientes = models.IntegerField()

    def __str__(self): # me sirve para ver en admin la info cargada

        return f"Es exportador: {self.exportando} | País de destino: {self.paisDestino} | Clientes: {self.clientes}"

class Convenio(models.Model): #con vista convenio/template convenio

    camara = models.CharField(max_length=40)
    actividad = models.CharField(max_length=40)

    def __str__(self): # me sirve para ver en admin la info cargada

        return f"Camara/Asocación: {self.camara} | Actividad: {self.actividad}"

class Documentacion(models.Model): #con vista documentacion

    formulario = models.IntegerField()
    detalleCompradores = models.IntegerField()

    def __str__(self): # me sirve para ver en admin la info cargada

        return f"Formulario n°: {self.formulario} | Detalle de Compradores: {self.detalleCompradores}"

class Siniestros(models.Model):

    fechaSiniestro=models.DateField()
    reclamado=models.BooleanField()
    montoImplicado=models.IntegerField()
    detalle=models.CharField(max_length=140)

    def __str__(self):

        return f"Fecha Siniestro: {self.fechaSiniestro} | Reclamado: {self.reclamado} | Monto implicado: {self.montoImplicado} | Detalle: {self.detalle}"

class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return f"ID: {self.usuario_id} | Usuario: {self.username} | email: {self.email}"

class Autenticacion(models.Model):
    usuario: Usuario
    password: models.CharField(max_length=20) 

class Cliente(models.Model):
    identification = models.OneToOneField("Usuario", null=True ,blank=True, on_delete=models.RESTRICT)
    polizas_id = models.ManyToManyField(poliza, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"ID Cliente: {self.identification}, Polizas: {self.polizas_id}"
    
class Autentication(models.Model):
    email: models.CharField(max_length=20)
    password: models.CharField(max_length=20)

class Cobertura(models.Model):

    tipo = models.CharField(max_length=20)
    numeroPoliza = models.OneToOneField(
        poliza, 
        on_delete=models.RESTRICT
        )
    fechaContratacion = models.DateField()
    fechaVigencia = models.DateField()
    detalle = models.CharField(max_length=40)

    def __str__(self):
        
         return f"Tipo de Cobertura: {self.tipo} | Poliza n°: {self.numeroPoliza} | Fecha alta: {self.fechaContratacion} | Vigencia hasta: {self.fechaVigencia} | Detalle: {self.detalle}"

