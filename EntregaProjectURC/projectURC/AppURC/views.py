from django.db.models.fields import CommaSeparatedIntegerField
from django.db import models
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from AppURC.models import *
from AppURC.forms import FormularioAsegurado, FormularioExportaciones, FormularioSiniestros, FormularioCoberturas
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages





def datosAsegurado(request):  # check
    
    data = Asegurado.objects.all()            
    context = {
        'asegurados' : data
    }
    
    return render(request, 'AppURC/ficha.html', context)


def coberturas(request):  # check

    return render(request, 'AppURC/coberturas.html')


def convenio(request):  # check

    return render(request, 'AppURC/convenio.html')


def documentacion(request):  # check

    return render(request, 'AppURC/documentacion.html')


def exportaciones(request):  # check

    return render(request, 'AppURC/exportaciones.html')


def showRegister(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
    else:
        form = UserCreationForm()

    params = {'form': form}
    return render(request, "register.html", context=params)


def formularioAsegurado(request):
    if request.method == 'POST':

        miFormulario = FormularioAsegurado(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            aseguradoInstancia = Asegurado(razonSocial=informacion["razonSocial"], cuit=informacion["cuit"])

            aseguradoInstancia.save()

            return render(request, 'AppURC/home.html')

    else:

        miFormulario = FormularioAsegurado()

    return render(request, 'AppURC/formularioAsegurado.html', {'miFormulario': miFormulario})


def busquedaDeAsegurado(request):
    return render(request, 'AppURC/busquedaDeAsegurado.html')


def buscarAseg(request):
    if request.GET["cuit"]:  # se fija si la request viene metodo GET con un "cuit" hace cosas

        cuit = request.GET["cuit"]  # guarda el nombre via get en una variable para python
        asegurados = Asegurado.objects.filter(
            cuit__icontains=cuit)  # busca los cuit en la BD, trayendo solo los que coincidan con la request (FILTRADOS)
        # si aparecen asegurados con esos cuit, los guarda en "asegurados

        return render(request, 'AppURC/resultadoBusquedaAseg.html',
                      {"asegurados": asegurados, "cuit": cuit})  # y se envían al resultado de la busqueda

    else:

        respuestaAsg = "Por favor verifica el cuit ingresado"

    return HttpResponse(respuestaAsg)


# TODO: Tomar tarea para mostrar una lista de coberturas.
# def readCoberturas(request):

# expos=export.objects.all() # traigo todas las exportaciones

# para ver las expo en html, hay que mandarlas como contexto a través deun diccionario

# dic = {"Exportaciones": expos}

# return render(request, 'AppURC/readExportaciones.html', dic)


# Vistas para solapa "Exportaciones y Destinos"
def readExportaciones(request):
    expos = export.objects.all()  # traigo todas las exportaciones

    # para ver las expo en html, hay que mandarlas como contexto a través deun diccionario

    dic = {"Exportaciones": expos}

    return render(request, 'AppURC/readExportaciones.html', dic)


def eliminarExportaciones(request, paisDestino_eliminar):
    eliminarPaisDestino = export.objects.get(paisDestino=paisDestino_eliminar)
    eliminarPaisDestino.delete()

    expos = export.objects.all()

    dic = {'Exportaciones': expos}

    return render(request, 'AppURC/readExportaciones.html', dic)


def editarExportaciones(request, paisDestino_editar):
    editarExportacion = export.objects.get(paisDestino=paisDestino_editar)

    if request.method == "POST":

        formulario = FormularioExportaciones(request.POST)

        print(formulario)

        if formulario.is_valid:

            informacion = formulario.cleaned_data

            editarExportacion.exportando = informacion["exportando"]
            # editarExportacion.paisDestino = informacion["paisDestino"]
            editarExportacion.clientes = informacion["clientes"]

            editarExportacion.save()

            return render(request, 'AppURC/home.html') 

        else:

            formulario = FormularioExportaciones(
                initial={'exportando': editarExportacion.exportando, 'paisDestino': editarExportacion.paisDestino,
                         'clientes': editarExportacion.clientes})

        return render(request, "AppURC/editarExportaciones.html",
                      {'formulario': formulario, 'paisDestino_editar': paisDestino_editar})


def formularioExportaciones(request):
    if request.method == 'POST':

        miFormulario2 = FormularioExportaciones(request.POST)

        print(miFormulario2)

        if miFormulario2.is_valid:
            informacion = miFormulario2.cleaned_data

            exportacionesInstancia = export(exportando=informacion["exportando"],
                                            paisDestino=informacion["paisDestino"], clientes=informacion["clientes"])

            exportacionesInstancia.save()

            return render(request, 'AppURC/readExportaciones.html')

    else:

        miFormulario2 = FormularioExportaciones()

    return render(request, 'AppURC/formularioExportaciones.html', {'miFormulario2': miFormulario2})


# Vistas para solapa "Registro de coberturas"

def formularioCoberturas(request):
    if request.method == 'POST':

        formulario = FormularioCoberturas(request.POST)

        print(formulario)

        if formulario.is_valid:
            informacion = formulario.cleaned_data

            coberturaInstancia = Cobertura(

                tipo=informacion["tipo"],
                numeroPoliza=informacion["numeroPoliza"],
                fechaContratacion=informacion["fechaContratacion"],
                fechaVigencia=informacion["fechaVigencia"],
                detalle=informacion["detalle"],

            )

            coberturaInstancia.save()
            cobert = Cobertura.objects.all()

            return render(request, 'AppURC/readCoberturas.html', {"Coberturas": cobert})

    else:

        formulario = FormularioCoberturas()

    return render(request, 'AppURC/formularioCoberturas.html', {'formulario': formulario})


def readCoberturas(request):
    cobert = Cobertura.objects.all()
        
    return render(request, "AppURC/readCoberturas.html", {"Coberturas": cobert})


# vistas para nueva solapa "Registro de Siniestros"

def formularioSiniestros(request):
    if request.method == 'POST':

        miFormulario = FormularioSiniestros(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            siniestrosInstancia = Siniestros(

                fechaSiniestro=informacion["fechaSiniestro"],

                reclamado=informacion["reclamado"],

                montoImplicado=informacion["montoImplicado"],

                detalle=informacion["detalle"],

            )

            siniestrosInstancia.save()

            return render(request, 'AppURC/home.html')

    else:

        miFormulario = FormularioSiniestros()

    return render(request, 'AppURC/formularioSiniestros.html', {'miFormulario': miFormulario})
