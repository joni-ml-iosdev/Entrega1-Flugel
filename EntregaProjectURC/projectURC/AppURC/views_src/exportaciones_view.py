
from django.shortcuts import render
from AppURC.forms import FormularioExportaciones
from AppURC.models import export



def formularioExportaciones(request):
    if request.method == 'POST':

        miFormulario2 = FormularioExportaciones(request.POST)

        print(miFormulario2)

        if miFormulario2.is_valid:
            informacion = miFormulario2.cleaned_data

            exportacionesInstancia = export(exportando=informacion["exportando"],
            paisDestino=informacion["paisDestino"], 
            clientes=informacion["clientes"])

            exportacionesInstancia.save()

            return render(request, 'AppURC/readExportaciones.html')
