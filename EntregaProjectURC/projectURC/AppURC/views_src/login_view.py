from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from AppURC.views_src import home_view

def show_login(request):
    """Mostramos la pantalla para loguearse"""
        # si esta loguado lo mandamos a la home
    if request.user.is_authenticated:
        return redirect('Home')
    
    if request.method == 'POST':
        execute_login(request)
    else:        
        params = {
            "title": "Iniciar Sesión",
            "inputTitleEmail": "Usuario",
            "inputTitlePassword": "Contraseña",
            "buttonTitleMainAction": "Iniciar"
        }
            
        return render(request, "AppURC/login.html", context=params)


def execute_login(request):
    """Ejecutamos el login y si el resultado es OK lo envamos a la Home, caso contrario
    mostraermos un mensaje custom 404
    """
    if request.method == 'POST':
        usernameInput = request.POST["usernameInput"]
        passwordInput = request.POST["inputPassword"]
        user = authenticate(request, username=usernameInput,password=passwordInput)    
        
        if user is not None:
            login(request, user=user)
            return redirect('Home')
        else:
            Http404("No pudimos loguear al usuario, vualva a intentar")


def logoutUser(request):
    logout(request)
    return redirect('login')