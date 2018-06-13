# Generated by Django 2.0.6 on 2018-06-11 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id_bodega', models.AutoField(primary_key=True, serialize=False)),
                ('direccion_bodega', models.CharField(max_length=100)),
                ('telefono_bodega', models.IntegerField()),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'bodega',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'categoria_producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('correo_empleado', models.CharField(max_length=200)),
                ('contrasenia_empleado', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoProducto',
            fields=[
                ('id_estado_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'estado_producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_de_barras', models.IntegerField()),
                ('nombre_producto', models.CharField(max_length=100)),
                ('detalle_producto', models.CharField(max_length=1000)),
                ('direccion_foto_producto', models.CharField(max_length=200)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoBodega',
            fields=[
                ('id_tipo_bodega', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_bodega', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'tipo_bodega',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoCargo',
            fields=[
                ('id_tipo_cargo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_cargo', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'tipo_cargo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoPrecio',
            fields=[
                ('id_tipo_precio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_precio', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'tipo_precio',
                'managed': False,
            },
        ),
    ]