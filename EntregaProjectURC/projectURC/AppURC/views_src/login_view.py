from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from AppURC.models import Usuario
from AppURC.views_src import home_view

def show_login(request):
    """Mostramos la pantalla para loguearse"""
    params = {
        "title": "Iniciar Sesión",
        "inputTitleEmail": "Correo electrónico",
        "inputTitlePassword": "Contraseña",
        "buttonTitleMainAction": "Iniciar"
    }
    return render(request, "AppURC/login.html", context=params)


def execute_login(request):
    """Ejecutamos el login y si el resultado es OK lo envamos a la Home, caso contrario
    mostraermos un mensaje custom 404
    """
    if not request.POST:
        raise Http404("Solicitud invalida")

    emailInputDone = request.POST["inputEmail"]
    passwordInputDone = request.POST["inputPassword"]
    userFound = get_object_or_404(Usuario, email=emailInputDone)
        
    if not userFound:
        raise Http404("No Usuario matches the given query.")

    if userFound.password == passwordInputDone:
        return home_view.show_home(request, userFound.usuario_id)
    else:
        raise Http404("Usuario o clave invalida")
