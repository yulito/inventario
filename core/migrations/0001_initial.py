# Generated by Django 3.2.4 on 2021-06-30 18:27

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
                ('nomCargo', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'idCargo',
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idComuna', models.IntegerField(primary_key=True, serialize=False)),
                ('nomComuna', models.CharField(blank=True, max_length=70, null=True)),
            ],
            options={
                'db_table': 'idComuna',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('idEstado', models.IntegerField(primary_key=True, serialize=False)),
                ('nomEstado', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'idEstado',
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('idModelo', models.AutoField(db_column='idModelo', primary_key=True, serialize=False)),
                ('nomModelo', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'idModelo',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.IntegerField(primary_key=True, serialize=False)),
                ('nomRegion', models.CharField(blank=True, max_length=70, null=True)),
            ],
            options={
                'db_table': 'idRegion',
            },
        ),
        migrations.CreateModel(
            name='tipo_dispositivo',
            fields=[
                ('idTipoDisp', models.IntegerField(db_column='idTipoDisp', primary_key=True, serialize=False)),
                ('nomTipo', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'idTipoDisp',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('Rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('apellido_pa', models.CharField(blank=True, max_length=30, null=True)),
                ('apellido_ma', models.CharField(blank=True, max_length=30, null=True)),
                ('cargoo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cargo')),
            ],
            options={
                'db_table': 'Rut',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('idSucursal', models.IntegerField(primary_key=True, serialize=False)),
                ('nomSucursal', models.CharField(blank=True, max_length=70, null=True)),
                ('direccion', models.CharField(blank=True, max_length=120, null=True)),
                ('comunaa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.comuna')),
            ],
            options={
                'db_table': 'idSucursal',
            },
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('idCorrel', models.IntegerField(primary_key=True, serialize=False)),
                ('nroSerie', models.CharField(max_length=20, unique=True)),
                ('comentario', models.CharField(blank=True, max_length=2000, null=True)),
                ('estadoo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estado')),
                ('modeloo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modelo')),
                ('rutt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
                ('sucursall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sucursal')),
                ('tipo_dispositivoo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipo_dispositivo')),
            ],
            options={
                'db_table': 'idCorrel',
            },
        ),
        migrations.AddField(
            model_name='comuna',
            name='regionn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.region'),
        ),
    ]