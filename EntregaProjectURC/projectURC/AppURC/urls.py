from django.urls import path
from AppURC import views

urlpatterns = [
    path('home',views.home, name='Home'),
    path('ficha',views.datosAsegurado, name='DatosAsegurado'),
    path('coberturas',views.coberturas, name='Coberturas'),
    path('contacto',views.contacto, name='Contacto'),
    path('documentos',views.documentacion, name='Documentacion'),
]