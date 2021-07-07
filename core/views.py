from django.shortcuts import render
from core.models import *

def index(request):
    print('estoy en el index')
    context ={}
    return render(request, 'core/principal.html', context)

def dispositivo_list(request):
    print('estoy en en listar dispositivo')
    disp = Dispositivo.objects.all()
    context ={'disp':disp}
    return render(request, 'core/administrador/dispositivo_list.html', context)

