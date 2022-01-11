
from django.shortcuts import render
from AppURC.forms import FormularioSiniestros
from AppURC.models import Siniestros



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


def leerSiniestros(request):

    siniestro = Siniestros.objects.all()

    return render(request,'AppURC/leerSiniestros.html',{"Siniestros":siniestro})
