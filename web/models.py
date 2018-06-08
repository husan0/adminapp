from django.db import models
# Create your models here.


class TipoCargo(models.Model):
    id_tipo_cargo = models.AutoField(primary_key=True)
    nombre_tipo_cargo = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_cargo'


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    correo_empleado = models.CharField(max_length=200)
    contrasenia_empleado = models.CharField(max_length=32)
    id_tipo_cargo = models.ForeignKey(TipoCargo, on_delete=models.CASCADE, db_column='id_tipo_cargo')

    class Meta:
        managed = False
        db_table = 'empleado'


class TipoBodega(models.Model):
    id_tipo_bodega = models.AutoField(primary_key=True)
    nombre_tipo_bodega = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_bodega'

class Bodega(models.Model):
    id_bodega = models.AutoField(primary_key=True)
    id_tipo_bodega = models.ForeignKey(TipoBodega, on_delete=models.CASCADE, db_column='id_tipo_bodega')
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


class TipoPrecio(models.Model):
    id_tipo_precio = models.AutoField(primary_key=True)
    nombre_tipo_precio = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_precio'


class EstadoProducto(models.Model):
    id_estado_producto = models.AutoField(primary_key=True)
    nombre_tipo = models.CharField(max_length=100)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'estado_producto'


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    codigo_de_barras = models.IntegerField()
    nombre_producto = models.CharField(max_length=100)
    id_categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE, db_column='id_categoria')
    id_estado_producto = models.ForeignKey(EstadoProducto, on_delete=models.CASCADE, db_column='id_estado_producto')
    detalle_producto = models.CharField(max_length=1000)
    direccion_foto_producto = models.CharField(max_length=200)
    activo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'producto'
