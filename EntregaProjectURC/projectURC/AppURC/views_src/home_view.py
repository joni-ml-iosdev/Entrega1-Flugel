from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from AppURC.models import Usuario

@login_required(login_url='login')
def home(request):

    return render(request, 'AppURC/home.html')