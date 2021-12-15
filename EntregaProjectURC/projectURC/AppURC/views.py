from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'AppURC/home.html')

def datosAsegurado(request):

    return render(request, 'AppURC/ficha.html')

def coberturas(request):

    return render(request, 'AppURC/coberturas.html')

def contacto(request):

    return render(request, 'AppURC/contacto.html')