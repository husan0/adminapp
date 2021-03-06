# Generated by Django 2.0.6 on 2018-06-12 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alerta',
            fields=[
                ('id_alerta', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_producto', models.IntegerField()),
                ('nombre_producto', models.CharField(max_length=100)),
                ('fecha_alerta', models.CharField(max_length=200)),
                ('tipo_alerta', models.CharField(max_length=50)),
                ('descripcion_alerta', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'alerta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content_type_id', models.IntegerField()),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_comuna', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleEstablecimientoVenta',
            fields=[
                ('id_establecimiento_venta', models.AutoField(primary_key=True, serialize=False)),
                ('id_establecimiento', models.IntegerField()),
                ('nombre_establecimiento', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'detalle_establecimiento_venta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id_detalle_factura', models.AutoField(primary_key=True, serialize=False)),
                ('rut_empleado', models.CharField(blank=True, max_length=10, null=True)),
                ('nombre_empleado', models.CharField(blank=True, max_length=100, null=True)),
                ('apellido_empleado', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre_producto', models.CharField(max_length=100)),
                ('cantidad_productos', models.IntegerField()),
                ('precio_unitario_producto', models.IntegerField()),
                ('total_impuesto', models.IntegerField()),
                ('total_venta', models.IntegerField()),
                ('nombre_establecimiento_venta', models.CharField(max_length=100)),
                ('fecha_venta', models.DateTimeField()),
            ],
            options={
                'db_table': 'detalle_factura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetallePrecioProducto',
            fields=[
                ('id_detalle_precio_producto', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'detalle_precio_producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('content_type_id', models.IntegerField(blank=True, null=True)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_factura', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_unidad', models.IntegerField()),
                ('fecha_venta', models.DateTimeField()),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'factura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_inventario', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_stock', models.IntegerField()),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'inventario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MedioPago',
            fields=[
                ('id_medio_pago', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_medio_pago', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'medio_pago',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id_pais', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_pais', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'pais',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id_provincia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_provincia', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'provincia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_region', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('no_sucursal', models.AutoField(primary_key=True, serialize=False)),
                ('rut_surcursal', models.CharField(max_length=11)),
                ('nombre_sucursal', models.CharField(max_length=100)),
                ('direccion_sucursal', models.CharField(max_length=100)),
                ('telefono_sucursal', models.IntegerField()),
                ('horario_de_atencion_sucursal', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'sucursal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('no_tienda', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tienda', models.CharField(max_length=100)),
                ('direccion_tienda', models.CharField(max_length=100)),
                ('contacto_tienda', models.CharField(max_length=100)),
                ('horario_atencion', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'tienda',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TiendaOnline',
            fields=[
                ('id_tienda_online', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tienda_online', models.CharField(max_length=100)),
                ('direccion_tienda_online', models.CharField(max_length=100)),
                ('contacto_tienda_online', models.CharField(max_length=200)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'tienda_online',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id_tipo_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_usuario', models.CharField(max_length=100)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'tipo_usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('rut_usuario', models.CharField(max_length=10)),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('apellido_usuario', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('correo_usuario', models.CharField(max_length=200)),
                ('contrasenia_usuario', models.CharField(max_length=32)),
                ('activo', models.IntegerField()),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
    ]
