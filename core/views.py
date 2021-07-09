from django.db.models.fields import AutoField
from django.http.response import JsonResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
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
    sucursa = Sucursal.objects.all()
    marc = Marca.objects.all()
    #faltan los otros atributos
    context ={'disp':disp,
              'tipo':tipo,
              'mode':mode,
              'sucursa':sucursa,
              'marc':marc}
    
    return render(request, 'core/administrador/dispositivo_list.html', context)

@csrf_exempt
def agregarDispositivo(request):
    if request.method == 'POST':
        nro = request.POST['Nro']
        coment = request.POST['Texto']
        nombredis = request.POST['Nom'] 
        modee = request.POST['Mod']
        estad = request.POST['Estado']
        run = request.POST['Usu']
        local = request.POST['Suc']
        marc = request.POST['Mar']

        dispositivo = Dispositivo()
        dispositivo.nroSerie = nro
        dispositivo.comentario = coment
        dispositivo.tipo_dispositivoo = int(nombredis)
        dispositivo.modeloo = int(modee)
        dispositivo.estadoo = int(estad)
        dispositivo.rutt = run
        dispositivo.sucursall = int(local)
        dispositivo.marcaa = int(marc)
        
        dispositivo.save()
        dispositivo = Dispositivo.objects.all()
        data = JsonResponse.dump(dispositivo)
        #return StreamingHttpResponse(data)
        return StreamingHttpResponse('{"ok":"True", "msg":"Se Agrego Correctamente"}', data)
        