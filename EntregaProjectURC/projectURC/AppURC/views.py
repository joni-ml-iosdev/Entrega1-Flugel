from django.shortcuts import render
from django.http import HttpResponse
from AppURC.models import Asegurado
from AppURC.forms import FormularioAsegurado


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

