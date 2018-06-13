# Generated by Django 2.0.6 on 2018-06-13 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alerta_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoEnvio',
            fields=[
                ('id_estado_envio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_estado_envio', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'estado_envio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PrecioDespacho',
            fields=[
                ('id_precio_despacho', models.AutoField(primary_key=True, serialize=False)),
                ('precio_por_comuna', models.IntegerField()),
                ('nombre_comuna', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'precio_despacho',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('numero_de_seguimiento', models.AutoField(primary_key=True, serialize=False)),
                ('ubicacion_actual_del_envio', models.CharField(max_length=200)),
                ('detalle_envio', models.CharField(blank=True, max_length=250, null=True)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'seguimiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoDeEntrega',
            fields=[
                ('id_tipo_de_entrega', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_entrega', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'tipo_de_entrega',
                'managed': False,
            },
        ),
    ]
