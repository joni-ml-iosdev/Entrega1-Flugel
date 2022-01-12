from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User, UserManager
from AppURC.models import Usuario
from AppURC.views_src import home_view
from AppURC.forms import UserRegistrationForm


        
def register(request):
    """Mostramos la pantalla para registrarse"""
    
    # si esta loguado lo mandamos a la home
    if request.user.is_authenticated:
        return redirect('Home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            messages.success(request, f'El usuario {user} fue creado con éxito') 
            
            return render(request, "AppURC/login.html")
    else:        
        emptyForm = UserRegistrationForm()
        context = {
            'form' : emptyForm
        }
        return render(request, "AppURC/register.html", context)