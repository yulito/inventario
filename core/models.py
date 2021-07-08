from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.fields import CharField

class Region(models.Model):
    idRegion = models.IntegerField(blank=False, null=False, primary_key=True)
    nomRegion = models.CharField(max_length=70, blank=True, null=True)
    class Meta:
        db_table = "region"

class Comuna(models.Model):
    idComuna = models.IntegerField(blank=False, null=False, primary_key=True)
    nomComuna = models.CharField(max_length=70, blank=True, null=True)
    regionn = models.ForeignKey(Region, blank=False, null=False, on_delete=models.CASCADE)
    class Meta:
        db_table = "comuna"

class Sucursal(models.Model):
    idSucursal = models.IntegerField(blank=False, null=False, primary_key=True)
    nomSucursal = models.CharField(max_length=70, blank=True, null=True)
    direccion = models.CharField(max_length=120, blank=True, null=True)
    comunaa = models.ForeignKey(Comuna,  blank=False, null=False, on_delete=models.CASCADE)
    class Meta:
        db_table = "sucursal"

class Cargo(models.Model):
    idCargo = models.AutoField(blank=False, null=False, primary_key=True)
    nomCargo = models.CharField(max_length=60, blank=True, null=True)
    class Meta:
        db_table = "cargo"

class Usuario(models.Model):
    Rut = models.CharField(max_length=10, blank=False, null=False, primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellido_pa = models.CharField(max_length=30, blank=True, null=True)
    apellido_ma = models.CharField(max_length=30, blank=True, null=True)
    cargoo = models.ForeignKey(Cargo,  blank=False, null=False, on_delete=models.CASCADE)
    class Meta:
        db_table = "usuario"

class tipo_dispositivo(models.Model):
    idTipoDisp = models.IntegerField(db_column='idTipoDisp', primary_key=True)
    nomTipo = models.CharField(max_length=30 , blank=True, null=True)
    class Meta:
        db_table = "tipo_dispositivo"

class Modelo(models.Model):
    idModelo = models.AutoField(db_column='idModelo', primary_key=True)
    nomModelo = models.CharField(max_length=60 , blank=True, null=True)
    class Meta:
        db_table = "modelo"

class Estado(models.Model):
    idEstado = models.IntegerField(blank=False, null=False, primary_key=True)
    nomEstado = models.CharField(max_length=20, blank=True, null=True)
    class Meta:
        db_table = "estado"

class Marca(models.Model):
    idMarca = models.IntegerField(db_column='idMarca', primary_key=True)
    nomMarca = models.CharField(max_length=20, blank=True, null=True)
    class Meta:
        db_table = "marca"

class Dispositivo(models.Model):
    idCorrel = models.AutoField(blank=False, null=False, primary_key=True) 
    nroSerie = models.CharField(max_length=20, blank=False, null=False, unique=True)
    nomDisp = models,CharField(max_length=30, blank=True, null=True, unique=True)
    comentario = models.CharField(max_length=2000, blank=True, null=True)
    tipo_dispositivoo = models.ForeignKey(tipo_dispositivo, blank=False, null=False, on_delete=models.CASCADE)
    modeloo = models.ForeignKey(Modelo, blank=False, null=False, on_delete=models.CASCADE)
    estadoo = models.ForeignKey(Estado, blank=False, null=False, on_delete=models.CASCADE)
    rutt = models.ForeignKey(Usuario, blank=True, null=True, on_delete=models.CASCADE)
    sucursall = models.ForeignKey(Sucursal, blank=False, null=False, on_delete=models.CASCADE)
    marcaa = models.ForeignKey(Marca, blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
        db_table = "dispositivo"

