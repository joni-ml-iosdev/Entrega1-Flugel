from django.shortcuts import render
from django.http import HttpResponse
from AppURC.models import Asegurado


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

        aseguradoInstancia = Asegurado (request.POST ["razonSocial"], request.POST["cuit"]) 

        aseguradoInstancia.save()

        return render(request, 'AppURC/home.html')

        
    return render(request, 'AppURC/formularioAsegurado.html')

