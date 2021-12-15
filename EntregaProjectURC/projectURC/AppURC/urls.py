from django.urls import path
from AppURC import views

urlpatterns = [
    path('home',views.home),
    path('ficha',views.datosAsegurado),
    path('coberturas',views.coberturas),
    path('contacto',views.contacto),
    path('documentos',views.documentacion),
]