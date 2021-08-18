import json
from django.db.models.fields import AutoField, NullBooleanField
from django.http.response import HttpResponse, HttpResponseServerError, JsonResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from core.models import *
from django.core import serializers

def index(request):
    print('estoy en el index')
    context ={}
    return render(request, 'core/principal.html', context)

@csrf_exempt
def dispositivo_list(request):
    print('estoy en en listar dispositivo')
    return render(request, 'core/administrador/dispositivo_list.html', listaDispo())

def listaDispo():
    disp = Dispositivo.objects.all()
    mode = Modelo.objects.all()
    sucursa = Sucursal.objects.all()
    usua = Usuario.objects.all()
    estad = Estado.objects.all()
    tip = tipo_dispositivo.objects.all()
    mar = Marca.objects.all()
    data ={'disp':disp,
            'usuario':usua,
            'modelo':mode,
            'sucursal':sucursa,
            'estado':estad,
            'tip':tip,
            'mar':mar} 
    return data

@csrf_exempt
def crearDispositivo(request):
    if request.method == 'POST':
        nro = request.POST['Nro'] 
        coment = request.POST['Texto']  
        modee = request.POST['Mod'] 
        _modelo = Modelo.objects.get(idModelo = modee)
        estad = request.POST['Estado']  
        _estado = Estado.objects.get(idEstado = estad)
        run = request.POST['Usu'] 
        if run != "":
            _rut = Usuario.objects.get(Rut = run)
        else:
            _rut = None

        local = request.POST['Suc']  
        _sucursal = Sucursal.objects.get(idSucursal = local)
        
        obj = Dispositivo.objects.create(
            nroSerie = nro,
            comentario = coment,
            modeloo = _modelo,
            estadoo = _estado,
            rutt = _rut,
            sucursall = _sucursal,
        )
        
        if obj.rutt != None:    
            usuario = obj.rutt.nombre
        else:
            usuario = " -- " 
            print(usuario)

        dispp = {
            'id':obj.idCorrel,
            'nro':obj.nroSerie,           
            'modelo':obj.modeloo.nomModelo,
            'marca':obj.modeloo.marcaa.nomMarca,
            'tipo':obj.modeloo.tipo_dispositivoo.nomTipo,
            'estado':obj.estadoo.nomEstado,
            'usuario':usuario          
        }
        data = {'dispp':dispp}
        return JsonResponse(data) 
    else:
         return HttpResponse('Faltan datos!!') 

@csrf_exempt
def buscarDispositivo(request):
    _id = request.POST['id']
    objdispositivo = Dispositivo.objects.get(idCorrel = _id)
    if objdispositivo.rutt != None:    
        usuario = objdispositivo.rutt.Rut
    else:
        usuario = ""           
    dispoo ={'id':objdispositivo.idCorrel,
                'serie':objdispositivo.nroSerie,
                'texto':objdispositivo.comentario,
                'modelo':objdispositivo.modeloo.nomModelo,
                'estado':objdispositivo.estadoo.idEstado,
                'rut':usuario,
                'sucursal':objdispositivo.sucursall.nomSucursal}

    ### Añade los select de modelo 
    datouno=[]
    for i in Modelo.objects.all():
        datouno.append({'idmod':i.idModelo, 
                    'nomMod':i.nomModelo,
                    'marcaa':i.marcaa.nomMarca,
                    'tipoo':i.tipo_dispositivoo.nomTipo
                    })   
    mode = {'datoI':datouno}

    '''
    ### Añade los select de estado
    datodos=[]
    for i in Estado.objects.all():
        datodos.append({'idEsta':i.idEstado, 
                    'nomEsta':i.nomEstado
                    })   
    esta = {'datoII':datodos}
    '''
    

    ### Añade los select de sucursal
    datotres=[]
    for i in Sucursal.objects.all():    #En vola hay que agregar todos lo atributos...
        datotres.append({'idsuc':i.idSucursal, 
                    'nombreSuc':i.nomSucursal
                    })   
    sucur = {'datoII':datotres}

    ### Junta todos los json y arreglos en un dato #  'esta':esta,
    data = {'dispoo':dispoo,
            'mode':mode,           
            'sucur':sucur
            }      

    return StreamingHttpResponse(json.dumps(data)) 

@csrf_exempt
def dispositivoActualizar(request):
    print('Estoy en dispositivoActualizar en Views.py')
    id_ = request.POST['idcorred']
    moded = request.POST['Moded']
    moded_ = Modelo.objects.get(nomModelo = moded)

    nroed_ = request.POST['Nroed']
    textoed_ = request.POST['Textoed']
    estadoed = request.POST['Estadoed']
    estadoed_ = Estado.objects.get(idEstado = estadoed)
    print(estadoed_.nomEstado)
    suced = request.POST['Suced']
    suced_ = Sucursal.objects.get(nomSucursal = suced)

    usued = request.POST['Usued']
    if usued != "":
        usuaed_ = Usuario.objects.get(Rut = usued)
    else:
        usuaed_ = None
      
    dispositivoo = Dispositivo()
    dispositivoo.idCorrel = id_
    dispositivoo.nroSerie = nroed_
    dispositivoo.comentario = textoed_
    dispositivoo.modeloo = moded_
    dispositivoo.estadoo = estadoed_
    dispositivoo.rutt = usuaed_
    dispositivoo.sucursall = suced_ 
    dispositivoo.save()

    data=[]
    for i in Dispositivo.objects.all():
        
        if i.rutt != None:    
            usuario = i.rutt.nombre
        else:
            usuario = " -- " 
            
        
        data.append({'corre':i.idCorrel, 
                    'serie':i.nroSerie,
                    'comentario':i.comentario,
                    'modelo':i.modeloo.nomModelo,
                    'estado':i.estadoo.nomEstado,
                    'marca':i.modeloo.marcaa.nomMarca,
                    'tipo':i.modeloo.tipo_dispositivoo.nomTipo,
                    'rut': usuario, #usuario i.rutt,
                    'sucursal':i.sucursall.nomSucursal
                    })

    return HttpResponse(json.dumps(data)) 

'''
def mostrarDispo(request):
    if request.method == 'GET':
        disp = Dispositivo.objects.all()

        #data = json.dumps(disp)
        #data ={'disp':list(disp)}
        #return JsonResponse(data)
        #return HttpResponse(data)
        tmpJson = serializers.serialize("json",disp)
        tmpObj = json.loads(tmpJson)       
        return HttpResponse(json.dumps(tmpObj))
        #return HttpResponse(tmpObj) //ESTA IGUAL FUNCIONA
'''   

######### CRUD PARA MARCA #########
@csrf_exempt
def marcas(request):
    print('estoy en MARCAS')
    marcaa = Marca.objects.all()
    data = {'marcaa':marcaa}
    return render(request, 'core/administrador/marcas.html', data)

@csrf_exempt
def crearMarca(request):
    print('estoy en CREAR MARCAS')
    _marca = request.POST['marca']
    if(_marca != ""):
        objmarc = Marca.objects.create(
        nomMarca = _marca
        )
        objmarc.save()
        marcaa ={'idmarca':objmarc.idMarca,
                'marca':objmarc.nomMarca}
        data = {'marcaa':marcaa}
        return JsonResponse(data)
    else:
        return HttpResponse('Faltan datos!!')   

@csrf_exempt
def buscarMarca(request):
    _idmarca = request.POST['idmarca']
    objmarca = Marca.objects.get(idMarca = _idmarca)
    marcaa ={'idmarca':objmarca.idMarca,
            'marca':objmarca.nomMarca}
    data = {'marcaa':marcaa}
    return JsonResponse(data)

@csrf_exempt
def marcaActualizar(request):
    print('Estoy en actualizar Marca en Views.py')
    _idmarca = request.POST['idmarca']
    _marca = request.POST['marca']
    marca = Marca()
    marca.idMarca = _idmarca
    marca.nomMarca = _marca
    marca.save()
    
    objmarca = list(Marca.objects.all().values_list())
    return HttpResponse(json.dumps(objmarca))

######### CRUD PARA TIPOS DE DATOS #########
@csrf_exempt
def tipos(request):
    print('estoy en VIEWS DE TIPOS DE DISPOSITIVOS')
    tipoo = tipo_dispositivo.objects.all()
    data = {'tipoo':tipoo}
    return render(request, 'core/administrador/tipos.html', data)

@csrf_exempt
def crearTipo(request):
    print('estoy en CREAR TIPO')
    _tipo = request.POST['tipo']
    if(_tipo != ""):
        objmarc = tipo_dispositivo.objects.create(
        nomTipo = _tipo
        )
        objmarc.save()
        tipoo ={'idTipo':objmarc.idTipoDisp,
                'tipo':objmarc.nomTipo}
        data = {'tipoo':tipoo}
        return JsonResponse(data)
    else:
        return HttpResponse('Faltan datos!!')  

@csrf_exempt
def buscarTipo(request):
    _idTipo = request.POST['idTipo']
    objmarca = tipo_dispositivo.objects.get(idTipoDisp = _idTipo)
    tipoo ={'idTipo':objmarca.idTipoDisp,
            'tipo':objmarca.nomTipo}
    data = {'tipoo':tipoo}
    return JsonResponse(data)

@csrf_exempt
def tipoActualizar(request):
    print('Estoy en tipoActualizar en Views.py')
    _idTipo = request.POST['idTipo']
    _tipo = request.POST['tipo']
    tipo = tipo_dispositivo()
    tipo.idTipoDisp = _idTipo
    tipo.nomTipo = _tipo
    tipo.save()
    
    objmarca = list(tipo_dispositivo.objects.all().values_list())
    return HttpResponse(json.dumps(objmarca)) 

######### CRUD PARA CARGO #########
@csrf_exempt
def cargo(request):
    print('estoy en VIEWS DE TIPOS DE DISPOSITIVOS')
    cargoo = Cargo.objects.all()
    data = {'cargoo':cargoo}
    return render(request, 'core/administrador/cargo.html', data)

@csrf_exempt
def crearCargo(request):
    print('estoy en CREAR CARGO')
    _cargo = request.POST['cargo']
    if(_cargo != ""):
        objcargo = Cargo.objects.create(
        nomCargo = _cargo
        )
        objcargo.save()
        cargoo ={'idCargo':objcargo.idCargo,
                'cargo':objcargo.nomCargo}
        data = {'cargoo':cargoo}
        return JsonResponse(data)
    else:
        return HttpResponse('Faltan datos!!')  

@csrf_exempt
def buscarCargo(request):
    _idCargo = request.POST['idCargo']
    objcargo = Cargo.objects.get(idCargo = _idCargo)
    cargoo ={'idCargo':objcargo.idCargo,
            'cargo':objcargo.nomCargo}
    data = {'cargoo':cargoo}
    return JsonResponse(data)

@csrf_exempt
def cargoActualizar(request):
    print('Estoy en tipoActualizar en Views.py')
    _idCargo = request.POST['idCargo']
    _cargo = request.POST['cargo']
    cargo = Cargo()
    cargo.idCargo = _idCargo
    cargo.nomCargo = _cargo
    cargo.save()
    
    objcargo = list(Cargo.objects.all().values_list())
    return HttpResponse(json.dumps(objcargo)) 

######### CRUD PARA USUARIO #########
@csrf_exempt
def usuarios(request):
    print('estoy en VIEWS DE TIPOS DE USUARIOS')
    usuarioo = Usuario.objects.all()
    cargo = Cargo.objects.all()
    data = {'usuarioo':usuarioo,
            'cargo':cargo}
    return render(request, 'core/administrador/usuario.html', data)

@csrf_exempt
def crearUsuario(request):
    _rut = request.POST['rut']
    _nombre = request.POST['nombre']
    _apepa = request.POST['apePa']
    _apema = request.POST['apeMa']
    _cargo = request.POST['cargo']
    #_cargoo = Cargo.objects.get(idCargo = _cargo)
    if((_rut != "") or (_nombre != "") or (_apepa != "") or (_apema != "") or (_cargo != "")):
        _cargoo = Cargo.objects.get(idCargo = _cargo)
        obj = Usuario.objects.create(
            Rut = _rut,
            nombre = _nombre,
            apellido_pa = _apepa,
            apellido_ma = _apema,
            cargoo = _cargoo
        )  
        user = {
            'rut':obj.Rut,
            'nombre':obj.nombre,
            'apePa':obj.apellido_pa,
            'apeMa':obj.apellido_ma,
            'cargo':obj.cargoo.nomCargo
        }
        data = {'user':user}
        return JsonResponse(data) 
    else:
         return HttpResponse('Faltan datos!!') 

@csrf_exempt
def buscarUsuario(request):
    _rut = request.POST['rut']
    objusuario = Usuario.objects.get(Rut = _rut)
    usuarioo ={'rut':objusuario.Rut,
                'nombre':objusuario.nombre,
                'apePa':objusuario.apellido_pa,
                'apeMa':objusuario.apellido_ma,
                'cargo':objusuario.cargoo.nomCargo}
    
    dato=[]
    for i in Cargo.objects.all():
        dato.append({'idCargo':i.idCargo, 
                    'nomCargo':i.nomCargo
                    })
    
    cargoo = {'dato':dato}

    data = {'usuarioo':usuarioo,
            'cargoo':cargoo}      

    return StreamingHttpResponse(json.dumps(data)) #StreamingHttpResponse se utiliza cuando se envias varios arreglos o listas distintas a la vez
   
@csrf_exempt
def usuarioActualizar(request):
    print('Estoy en tipoActualizar en Views.py')
    _rut = request.POST['rut']
    _nombre = request.POST['nombre']
    _apepa = request.POST['apePa']
    _apema = request.POST['apeMa']
    _cargo = request.POST['cargo']
    _cargoo = Cargo.objects.get(nomCargo = _cargo)
    
    usuarioo = Usuario()
    usuarioo.Rut = _rut
    usuarioo.nombre = _nombre
    usuarioo.apellido_pa = _apepa
    usuarioo.apellido_ma = _apema
    usuarioo.cargoo = _cargoo
    usuarioo.save()

    data=[]
    for i in Usuario.objects.all():
        data.append({'rut':i.Rut, 
                    'nombre':i.nombre,
                    'apePa':i.apellido_pa,
                    'apeMa':i.apellido_ma,
                    'cargo':i.cargoo.nomCargo
                    })

    return HttpResponse(json.dumps(data)) 

######### CRUD PARA MODELO #########

@csrf_exempt
def modelos(request):
    print('estoy en el modelos')
    modelo = Modelo.objects.all()
    marca = Marca.objects.all()
    tipo = tipo_dispositivo.objects.all()
    data = {'modelo':modelo,
            'marca':marca,
            'tipo':tipo}
    return render(request, 'core/administrador/modelos.html', data)  

@csrf_exempt
def crearModelo(request):
    _nomMod= request.POST['nombreMod']
    _marMod = request.POST['marcaMod']
    _modTipo = request.POST['modeloTipo']

    if((_nomMod != "") or (_marMod != "") or (_modTipo != "") ):
        _marca = Marca.objects.get(idMarca = _marMod)
        _tipo = tipo_dispositivo.objects.get(idTipoDisp = _modTipo)

        objmod = Modelo.objects.create(
            nomModelo = _nomMod,
            marcaa = _marca,
            tipo_dispositivoo = _tipo,
            )  
        dato = {
            'idModelo':objmod.idModelo,
            'nombre':objmod.nomModelo,
            'marca':objmod.marcaa.nomMarca,
            'tipo':objmod.tipo_dispositivoo.nomTipo
        }
        data = {'modelo':dato}
        return JsonResponse(data) 
    else:
         return HttpResponse('Faltan datos!!') 

@csrf_exempt
def buscarModelo(request):
    _id = request.POST['idModelo']
    objmodelo = Modelo.objects.get(idModelo = _id)
    modeloo ={'idModelo':objmodelo.idModelo,
                'nombre':objmodelo.nomModelo,
                'marca':objmodelo.marcaa.nomMarca,
                'tipo':objmodelo.tipo_dispositivoo.nomTipo
                }
    
    datom=[]
    for i in Marca.objects.all():
        datom.append({'idMarca':i.idMarca, 
                    'nomMarca':i.nomMarca
                    })

    datot=[]
    for i in tipo_dispositivo.objects.all():
        datot.append({'idTipoDisp':i.idTipoDisp, 
                    'nomTipo':i.nomTipo
                    })
    
    _marca_ = {'datom':datom}
    _tipo_ = {'tipod':datot}

    data = {'modeloo':modeloo,
            'marcaa':_marca_,
            'tipoo':_tipo_}      

    return StreamingHttpResponse(json.dumps(data)) #StreamingHttpResponse se utiliza cuando se envias varios arreglos o listas distintas a la vez
   
@csrf_exempt
def modeloActualizar(request):
    print('Estoy en modeloActualizar en Views.py')
    _idmod = request.POST['modeloed']
    _nommod = request.POST['nombreModed']
    _marcaed = request.POST['marcaModed']
    _marcaa = Marca.objects.get(nomMarca = _marcaed)
    _modtipo = request.POST['modeloTipoed']
    _tipoo = tipo_dispositivo.objects.get(nomTipo = _modtipo)

    modelo = Modelo()
    modelo.idModelo = _idmod
    modelo.nomModelo = _nommod
    modelo.marcaa = _marcaa
    modelo.tipo_dispositivoo = _tipoo
    modelo.save()
    
    data=[]
    for i in Modelo.objects.all():
        data.append({'idMod':i.idModelo, 
                    'nombremod':i.nomModelo,
                    'marcamod':i.marcaa.nomMarca,
                    'tipomod':i.tipo_dispositivoo.nomTipo,
                    })

    return HttpResponse(json.dumps(data)) 
