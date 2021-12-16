from django.urls import path
from AppURC import views

urlpatterns = [
    path('home',views.home, name='Home'),

    path('ficha',views.datosAsegurado, name='DatosAsegurado'),

    path('coberturas',views.coberturas, name='Coberturas'),

    path('convenio',views.convenio, name='Convenio'),

    path('documentacion',views.documentacion, name='Documentacion'),

    path('exportaciones',views.exportaciones, name='Exportaciones'),

    
]