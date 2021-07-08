from django.shortcuts import render
from core.models import *

def index(request):
    print('estoy en el index')
    context ={}
    return render(request, 'core/principal.html', context)

def dispositivo_list(request):
    print('estoy en en listar dispositivo')
    disp = Dispositivo.objects.all()
    tipo = tipo_dispositivo.objects.all()
    mode = Modelo.objects.all()
    #estad = Estado.objects.all()
    sucursa = Sucursal.objects.all()
    marc = Marca.objects.all()
    context ={'disp':disp,
              'tipo':tipo,
              'mode':mode,

              'sucursa':sucursa,
              'marc':marc}
    return render(request, 'core/administrador/dispositivo_list.html', context)

def agregarDispositivo(request):
    pass