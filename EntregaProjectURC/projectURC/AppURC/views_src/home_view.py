from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from AppURC.models import Usuario

def show_home(request, userId: int = 0): 
    ''' Show home
    Mostramos la vista de home y chequeamos su user id
    '''
    
    if request.method == 'POST' and userId !=0:
        user = get_object_or_404(Usuario, usuario_id=userId)
             
        contextHome = {
            "name":user.username
        }
        
        return render(request, 'AppURC/home.html', context=contextHome)
    
    if request.method == 'GET':

        return render(request, 'AppURC/home.html')

def home(request):

    return render(request, 'AppURC/home.html')