from django.urls import path
from AppURC import views
from .views_src import home_view, login_view, exportaciones_view, siniestros_view, register_view

urlpatterns = [
    path('home', home_view.home, name='Home'),

    path('ficha', views.datosAsegurado, name='DatosAsegurado'),

    path('coberturas', views.coberturas, name='Coberturas'),

    path('convenio', views.convenio, name='Convenio'),

    path('documentacion', views.documentacion, name='Documentacion'),

    path('exportaciones', views.exportaciones, name='Exportaciones'),

    path('formularioAsegurado', views.formularioAsegurado, name='FormularioAsegurado'),

    path('formularioExportaciones', views.formularioExportaciones, name='FormularioExportaciones'),

    path('busquedaDeAsegurado', views.busquedaDeAsegurado, name='BusquedaDeAsegurado'),

    path('buscarAseg/', views.buscarAseg),

    path('readExportaciones', views.readExportaciones, name='ReadExportaciones'),

    path('eliminarExportaciones/<paisDestino_eliminar>/', views.eliminarExportaciones, name='EliminarExportaciones'),

    path('editarExportaciones/<paisDestino_editar>/', views.editarExportaciones, name='EditarExportaciones'),

    path('login/', login_view.show_login, name='login'),
    
    path('execute-login/', login_view.execute_login, name='execute-login'),

    path('logout/', login_view.logoutUser, name='logout'),

    path('readCoberturas/', views.readCoberturas, name='ReadCoberturas'),

    path('formularioCoberturas', views.formularioCoberturas, name="FormularioCoberturas"),

    path('formularioSiniestros', siniestros_view.formularioSiniestros, name='FormularioSiniestros'),

    path('leerSiniestros/',siniestros_view.leerSiniestros,name="leerSiniestros"),
    
    path('register/',register_view.register,name="register"),


]
