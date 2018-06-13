# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alerta(models.Model):
    id_alerta = models.AutoField(primary_key=True)
    codigo_producto = models.IntegerField()
    id_inventario = models.ForeignKey('Inventario', models.DO_NOTHING, db_column='id_inventario')
    nombre_producto = models.CharField(max_length=100)
    fecha_alerta = models.CharField(max_length=200)
    tipo_alerta = models.CharField(max_length=50)
    descripcion_alerta = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'alerta'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Bodega(models.Model):
    id_bodega = models.AutoField(primary_key=True)
    id_tipo_bodega = models.ForeignKey('TipoBodega', models.DO_NOTHING, db_column='id_tipo_bodega')
    direccion_bodega = models.CharField(max_length=100)
    telefono_bodega = models.IntegerField()
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bodega'


class CategoriaProducto(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categoria_producto'


class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    id_provincia = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='id_provincia')
    nombre_comuna = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comuna'


class DetalleEstablecimientoVenta(models.Model):
    id_establecimiento_venta = models.AutoField(primary_key=True)
    id_establecimiento = models.IntegerField()
    nombre_establecimiento = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_establecimiento_venta'


class DetalleFactura(models.Model):
    id_detalle_factura = models.AutoField(primary_key=True)
    id_factura = models.ForeignKey('Factura', models.DO_NOTHING, db_column='id_factura')
    rut_empleado = models.CharField(max_length=10, blank=True, null=True)
    nombre_empleado = models.CharField(max_length=100, blank=True, null=True)
    apellido_empleado = models.CharField(max_length=100, blank=True, null=True)
    codigo_de_barras = models.ForeignKey('Producto', models.DO_NOTHING, db_column='codigo_de_barras')
    nombre_producto = models.CharField(max_length=100)
    cantidad_productos = models.IntegerField()
    precio_unitario_producto = models.IntegerField()
    total_impuesto = models.IntegerField()
    total_venta = models.IntegerField()
    nombre_establecimiento_venta = models.CharField(max_length=100)
    fecha_venta = models.DateTimeField()
    direccion_entrega = models.CharField(max_length=500, blank=True, null=True)
    precio_despacho = models.IntegerField(blank=True, null=True)
    nombre_comuna_entrega = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_factura'


class DetallePrecioProducto(models.Model):
    id_detalle_precio_producto = models.AutoField(primary_key=True)
    codigo_de_barras = models.ForeignKey('Producto', models.DO_NOTHING, db_column='codigo_de_barras')
    precio = models.IntegerField()
    id_tipo_precio = models.ForeignKey('TipoPrecio', models.DO_NOTHING, db_column='id_tipo_precio')
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_precio_producto'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    rut_empleado = models.CharField(max_length=10)
    nombre_empleado = models.CharField(max_length=100)
    apellido_empleado = models.CharField(max_length=100)
    direccion_empleado = models.CharField(max_length=100)
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    correo_empleado = models.CharField(max_length=100)
    contrasenia_empleado = models.CharField(max_length=32)
    id_tipo_cargo = models.ForeignKey('TipoCargo', models.DO_NOTHING, db_column='id_tipo_cargo')
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'


class EstadoEnvio(models.Model):
    id_estado_envio = models.AutoField(primary_key=True)
    nombre_estado_envio = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'estado_envio'


class EstadoProducto(models.Model):
    id_estado_producto = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'estado_producto'


class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    rut_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='rut_usuario')
    rut_vendedor = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='rut_vendedor', blank=True, null=True)
    codigo_de_barras = models.ForeignKey('Producto', models.DO_NOTHING, db_column='codigo_de_barras')
    cantidad_unidad = models.IntegerField()
    nombre_establecimiento_venta = models.ForeignKey(DetalleEstablecimientoVenta, models.DO_NOTHING, db_column='nombre_establecimiento_venta')
    id_medio_pago = models.ForeignKey('MedioPago', models.DO_NOTHING, db_column='id_medio_pago')
    id_tipo_precio = models.ForeignKey('TipoPrecio', models.DO_NOTHING, db_column='id_tipo_precio')
    fecha_venta = models.DateTimeField()
    id_tipo_de_entrega = models.ForeignKey('TipoDeEntrega', models.DO_NOTHING, db_column='id_tipo_de_entrega')
    id_precio_despacho = models.ForeignKey('PrecioDespacho', models.DO_NOTHING, db_column='id_precio_despacho', blank=True, null=True)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'factura'


class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    codigo_de_barras = models.ForeignKey('Producto', models.DO_NOTHING, db_column='codigo_de_barras')
    id_bodega = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='id_bodega')
    cantidad_stock = models.IntegerField()
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inventario'


class MedioPago(models.Model):
    id_medio_pago = models.AutoField(primary_key=True)
    nombre_medio_pago = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medio_pago'


class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pais'


class PrecioDespacho(models.Model):
    id_precio_despacho = models.AutoField(primary_key=True)
    precio_por_comuna = models.IntegerField()
    nombre_comuna = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'precio_despacho'


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    codigo_de_barras = models.IntegerField()
    nombre_producto = models.CharField(max_length=100)
    id_categoria = models.ForeignKey(CategoriaProducto, models.DO_NOTHING, db_column='id_categoria')
    id_estado_producto = models.ForeignKey(EstadoProducto, models.DO_NOTHING, db_column='id_estado_producto')
    detalle_producto = models.CharField(max_length=1000)
    direccion_foto_producto = models.CharField(max_length=200)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'producto'


class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')
    nombre_provincia = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'provincia'


class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=100)
    id_pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='id_pais')
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'region'


class Seguimiento(models.Model):
    numero_de_seguimiento = models.AutoField(primary_key=True)
    id_estado_envio = models.ForeignKey(EstadoEnvio, models.DO_NOTHING, db_column='id_estado_envio')
    id_detalle_factura = models.ForeignKey(DetalleFactura, models.DO_NOTHING, db_column='id_detalle_factura')
    ubicacion_actual_del_envio = models.CharField(max_length=200)
    detalle_envio = models.CharField(max_length=250, blank=True, null=True)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'seguimiento'


class Sucursal(models.Model):
    no_sucursal = models.AutoField(primary_key=True)
    rut_surcursal = models.CharField(max_length=11)
    nombre_sucursal = models.CharField(max_length=100)
    direccion_sucursal = models.CharField(max_length=100)
    telefono_sucursal = models.IntegerField()
    horario_de_atencion_sucursal = models.CharField(max_length=100)
    rut_jefe_sucursal = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='rut_jefe_sucursal')
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    id_bodega_sucursal = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='id_bodega_sucursal')
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class Tienda(models.Model):
    no_tienda = models.AutoField(primary_key=True)
    nombre_tienda = models.CharField(max_length=100)
    direccion_tienda = models.CharField(max_length=100)
    contacto_tienda = models.CharField(max_length=100)
    horario_atencion = models.CharField(max_length=100)
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    rut_jefe_tienda = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='rut_jefe_tienda')
    id_bodega_tienda = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='id_bodega_tienda')
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tienda'


class TiendaOnline(models.Model):
    id_tienda_online = models.AutoField(primary_key=True)
    nombre_tienda_online = models.CharField(max_length=100)
    direccion_tienda_online = models.CharField(max_length=100)
    contacto_tienda_online = models.CharField(max_length=200)
    rut_encargado_tienda_online = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='rut_encargado_tienda_online')
    id_bodega_online = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='id_bodega_online')
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tienda_online'


class TipoBodega(models.Model):
    id_tipo_bodega = models.AutoField(primary_key=True)
    nombre_tipo_bodega = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_bodega'


class TipoCargo(models.Model):
    id_tipo_cargo = models.AutoField(primary_key=True)
    nombre_tipo_cargo = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_cargo'


class TipoDeEntrega(models.Model):
    id_tipo_de_entrega = models.AutoField(primary_key=True)
    nombre_tipo_entrega = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_de_entrega'


class TipoPrecio(models.Model):
    id_tipo_precio = models.AutoField(primary_key=True)
    nombre_tipo_precio = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_precio'


class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    nombre_tipo_usuario = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    rut_usuario = models.CharField(max_length=10)
    nombre_usuario = models.CharField(max_length=100)
    apellido_usuario = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    correo_usuario = models.CharField(max_length=200)
    contrasenia_usuario = models.CharField(max_length=32)
    tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='tipo_usuario')
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'
