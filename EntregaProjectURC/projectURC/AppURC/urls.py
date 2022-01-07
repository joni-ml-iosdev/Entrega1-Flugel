from django.urls import path
from AppURC import views

urlpatterns = [
    path('home',views.home, name='Home'),

    path('ficha',views.datosAsegurado, name='DatosAsegurado'),

    path('coberturas',views.coberturas, name='Coberturas'),

    path('convenio',views.convenio, name='Convenio'),

    path('documentacion',views.documentacion, name='Documentacion'),

    path('exportaciones',views.exportaciones, name='Exportaciones'),

    path('formularioAsegurado',views.formularioAsegurado, name='FormularioAsegurado'),

    path('formularioExportaciones',views.formularioExportaciones, name='FormularioExportaciones'),

    path('formularioSiniestros',views.formularioSiniestros, name='FormularioSiniestros'),
    
    path('busquedaDeAsegurado',views.busquedaDeAsegurado, name='BusquedaDeAsegurado'),

    path('buscarAseg/', views.buscarAseg),
    
    path('readExportaciones', views.readExportaciones, name='ReadExportaciones' ),

    path('eliminarExportaciones/<paisDestino_eliminar>/', views.eliminarExportaciones, name='EliminarExportaciones' ),

    path('editarExportaciones/<paisDestino_editar>/', views.editarExportaciones, name='EditarExportaciones' ),

    path('login/',views.showLogin, name='login'),

    path('executeLogin/', views.executeLogin),

    path('register/', views.showRegister),

]