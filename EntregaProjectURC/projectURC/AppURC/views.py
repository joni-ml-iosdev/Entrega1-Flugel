from django.shortcuts import render
from django.http import HttpResponse
from AppURC.models import Asegurado,export,Siniestros
from AppURC.forms import FormularioAsegurado, FormularioExportaciones, FormularioSiniestros


def home(request): #check

    return render(request, 'AppURC/home.html')

def datosAsegurado(request): #check

    return render(request, 'AppURC/ficha.html')

def coberturas(request): #check

    return render(request, 'AppURC/coberturas.html')

def convenio(request): #check

    return render(request, 'AppURC/convenio.html')

def documentacion(request): #check

    return render(request, 'AppURC/documentacion.html')

def exportaciones(request): #check

    return render(request, 'AppURC/exportaciones.html')

def formularioAsegurado(request):

    
    if request.method == 'POST':

        miFormulario = FormularioAsegurado (request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            aseguradoInstancia = Asegurado (razonSocial=informacion["razonSocial"], cuit=informacion["cuit"]) 

            aseguradoInstancia.save()

            return render(request, 'AppURC/home.html')

    else:

        miFormulario= FormularioAsegurado()        
        
    return render(request, 'AppURC/formularioAsegurado.html',{'miFormulario':miFormulario})

def formularioExportaciones(request):

    
    if request.method == 'POST':

        miFormulario2 = FormularioExportaciones (request.POST)

        print(miFormulario2)

        if miFormulario2.is_valid:

            informacion = miFormulario2.cleaned_data

            exportacionesInstancia = export (exportando=informacion["exportando"], paisDestino=informacion["paisDestino"], clientes=informacion["clientes"]) 

            exportacionesInstancia.save()

            return render(request, 'AppURC/home.html')

    else:

        miFormulario2= FormularioExportaciones()        
        
    return render(request, 'AppURC/formularioExportaciones.html',{'miFormulario2':miFormulario2})

def busquedaDeAsegurado(request):

    return render(request, 'AppURC/busquedaDeAsegurado.html')

def buscarAseg(request):
    

    if request.GET["cuit"]:

        #respuestaAsg = f"Se esta buscando a {request.GET['cuit']}"
        cuit = request.GET["cuit"]
        razonSocial = Asegurado.objects.filter(cuit__icontains=cuit)

        return render(request, 'AppURC/resultadoBusquedaAseg.html',{"Razon Social":razonSocial,"Cuit":cuit})

    else:
        
        respuestaAsg = "Por favor verifica el cuit ingresado"

    return HttpResponse(respuestaAsg)

def formularioSiniestros(request):

        
    if request.method == 'POST':

        miFormulario = FormularioSiniestros (request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            siniestrosInstancia = Siniestros (

                fechaSiniestro=informacion["fechaSiniestro"],

                reclamado=informacion["reclamado"],

                montoImplicado=informacion["montoImplicado"],
                
                detalle=informacion["detalle"],

            ) 

            siniestrosInstancia.save()

            return render(request, 'AppURC/home.html')

    else:

        miFormulario= FormularioSiniestros()        
        
    return render(request, 'AppURC/formularioSiniestros.html',{'miFormulario':miFormulario})