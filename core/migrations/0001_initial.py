# Generated by Django 3.2.4 on 2021-08-03 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('idCargo', models.AutoField(primary_key=True, serialize=False)),
                ('nomCargo', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'cargo',
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idComuna', models.IntegerField(primary_key=True, serialize=False)),
                ('nomComuna', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'comuna',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('idEstado', models.IntegerField(primary_key=True, serialize=False)),
                ('nomEstado', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'estado',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idMarca', models.AutoField(db_column='idMarca', primary_key=True, serialize=False)),
                ('nomMarca', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'marca',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.IntegerField(primary_key=True, serialize=False)),
                ('nomRegion', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='tipo_dispositivo',
            fields=[
                ('idTipoDisp', models.AutoField(db_column='idTipoDisp', primary_key=True, serialize=False)),
                ('nomTipo', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tipo_dispositivo',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('Rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido_pa', models.CharField(blank=True, max_length=30, null=True)),
                ('apellido_ma', models.CharField(blank=True, max_length=30, null=True)),
                ('cargoo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cargo')),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('idSucursal', models.IntegerField(primary_key=True, serialize=False)),
                ('nomSucursal', models.CharField(max_length=70)),
                ('direccion', models.CharField(max_length=120)),
                ('comunaa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.comuna')),
            ],
            options={
                'db_table': 'sucursal',
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('idModelo', models.AutoField(db_column='idModelo', primary_key=True, serialize=False)),
                ('nomModelo', models.CharField(max_length=60)),
                ('marcaa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.marca')),
                ('tipo_dispositivoo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipo_dispositivo')),
            ],
            options={
                'db_table': 'modelo',
            },
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('idCorrel', models.AutoField(primary_key=True, serialize=False)),
                ('nroSerie', models.CharField(max_length=20, unique=True)),
                ('comentario', models.CharField(blank=True, max_length=2000, null=True)),
                ('estadoo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estado')),
                ('modeloo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modelo')),
                ('rutt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
                ('sucursall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sucursal')),
            ],
            options={
                'db_table': 'dispositivo',
            },
        ),
        migrations.AddField(
            model_name='comuna',
            name='regionn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.region'),
        ),
    ]
