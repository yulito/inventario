# Generated by Django 3.2.4 on 2021-06-30 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cargo',
            table='cargo',
        ),
        migrations.AlterModelTable(
            name='comuna',
            table='comuna',
        ),
        migrations.AlterModelTable(
            name='dispositivo',
            table='dispositivo',
        ),
        migrations.AlterModelTable(
            name='estado',
            table='estado',
        ),
        migrations.AlterModelTable(
            name='modelo',
            table='modelo',
        ),
        migrations.AlterModelTable(
            name='region',
            table='region',
        ),
        migrations.AlterModelTable(
            name='sucursal',
            table='sucursal',
        ),
        migrations.AlterModelTable(
            name='tipo_dispositivo',
            table='tipo_dispositivo',
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='usuario',
        ),
    ]