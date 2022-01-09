from django.urls import path
from AppURC import views
from .views_src import home_view, login_view

urlpatterns = [
    path('home/<int:loginId>', home_view.show_home, name='Home'),

    path('<int:loginId>', home_view.show_home, name='Home'),
    
    path('', home_view.show_home, name='Home'),

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

    path('execute_login/', login_view.execute_login, name='execute_login'),

    path('readCoberturas/', views.readCoberturas, name='ReadCoberturas'),

    path('formularioCoberturas', views.formularioCoberturas, name="FormularioCoberturas"),

    path('formularioSiniestros', views.formularioSiniestros, name='FormularioSiniestros'),

]
