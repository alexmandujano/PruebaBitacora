# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-24 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FECHA', models.DateField()),
                ('FECHA_ENVIO', models.DateField()),
                ('H_RECEPCION', models.TimeField()),
                ('H_INICIO', models.TimeField()),
                ('H_FIN', models.TimeField()),
                ('ASUNTO', models.TextField()),
                ('DETALLLE', models.TextField()),
                ('USUARIO_S', models.CharField(max_length=15)),
                ('USUARIO_R', models.CharField(max_length=15)),
                ('USUARIO_A', models.CharField(max_length=15)),
                ('USUARIO', models.CharField(max_length=15)),
                ('OTRA_AREA', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMBRE', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Scategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMBRE', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMBRE', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Herramienta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMBRE', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Medio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMBRE', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATEGORIA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bitacora.Categoria')),
                ('DETALLE_SCATEGORIA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bitacora.Detalle_Scategoria')),
                ('HERRAMIENTA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bitacora.Herramienta')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMBRE', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='opcion',
            name='SUB_CATEGORIA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bitacora.Sub_categoria'),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='ESTADO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bitacora.Estado'),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='MEDIO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bitacora.Medio'),
        ),
        migrations.AddField(
            model_name='bitacora',
            name='OPCION',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bitacora.Opcion'),
        ),
    ]
