from django.contrib import admin
from .models import *
from .src.models import *
# Register your models here.
#usuario_admin
#

admin.site.register(poliza)

admin.site.register(Asegurado)

admin.site.register(export)

admin.site.register(Convenio)

admin.site.register(Documentacion)

admin.site.register(Siniestros)

admin.site.register(Coberturas)

admin.site.register(Usuario)

admin.site.register(Cliente)

admin.site.register(Autentication)



