#from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
	path('index', views.index, name='index'),
	##### DISPOSITIVO #####
	path('dispositivo_list', views.dispositivo_list, name='dispositivo_list'),
	path('crearDispositivo', views.crearDispositivo, name='crearDispositivo'),
	path('listaDispo', views.listaDispo, name='listaDispo'), 
	path('buscarDispositivo', views.buscarDispositivo, name='buscarDispositivo'),
	path('dispositivoActualizar', views.dispositivoActualizar, name='dispositivoActualizar'),

	#path('mostrarDispo', views.mostrarDispo, name='mostrarDispo'),
	##### MARCAS #####
	path('marcas', views.marcas, name='marcas'),
	path('crearMarca', views.crearMarca, name='crearMarca'),
	path('buscarMarca', views.buscarMarca, name='buscarMarca'), 
	path('marcaActualizar', views.marcaActualizar, name='marcaActualizar'),
	##### TIPOS DE DISPOSITIVOS #####
	path('tipos', views.tipos, name='tipos'), 
	path('crearTipo', views.crearTipo, name='crearTipo'),
	path('buscarTipo', views.buscarTipo, name='buscarTipo'),
	path('tipoActualizar', views.tipoActualizar, name='tipoActualizar'),
	##### CARGO #####
	path('cargo', views.cargo, name='cargo'),
	path('crearCargo', views.crearCargo, name='crearCargo'),
	path('buscarCargo', views.buscarCargo, name='buscarCargo'),
	path('cargoActualizar', views.cargoActualizar, name='cargoActualizar'),
	##### USUARIO #####
	path('usuarios', views.usuarios, name='usuarios'),
	path('crearUsuario', views.crearUsuario, name='crearUsuario'),
	path('buscarUsuario', views.buscarUsuario, name='buscarUsuario'),
	path('usuarioActualizar', views.usuarioActualizar, name='usuarioActualizar'),
	##### MODELO #####
	path('modelos', views.modelos, name='modelos'), 
	path('crearModelo', views.crearModelo, name='crearModelo'),
	path('buscarModelo', views.buscarModelo, name='buscarModelo'),
	path('modeloActualizar', views.modeloActualizar, name='modeloActualizar'),
]	
