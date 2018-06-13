from django.shortcuts import render
from django.contrib import messages
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from django.db import connection

from .models import *


#------------------------------------------- VIEWS -------------------------------------------------------------


def index(request):
    if 'user' in request.session:
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')


def logout(request):
    del request.session['user']
    messages.warning(request, 'Desconectado exitosamente')
    return render(request, 'login.html')


def add(request):
    if 'user' in request.session:
        contexts = {
            'ListaC': CategoriaProducto.objects.all(),
            'ListaE': EstadoProducto.objects.all(),
            'listaB': Bodega.objects.all()
        }
        return render(request, 'agregar.html', contexts)
    else:
        return render(request, 'login.html')


def search(request):
    if 'user' in request.session:
        return render(request, 'buscar.html')
    else:
        return render(request, 'login.html')


def delete(request):
    if 'user' in request.session:
        return render(request, 'eliminar.html')
    else:
        return render(request, 'login.html')


def list(request):
    if 'user' in request.session:
        context = {
            "productos": listarProductos()
        }
        return render(request, 'listar.html', context)
    else:
        return render(request, 'login.html')


def update(request):
    if 'user' in request.session:
        return render(request, 'modificar.html')
    else:
        return render(request, 'login.html')

#------------------------------------------- FUNCTIONS -------------------------------------------------------------


def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        empleado = Empleado.objects.all()
        for empleados in empleado:
            if empleados.correo_empleado == username and empleados.contrasenia_empleado == password:
                request.session["user"] = username
                return render(request, 'index.html', {"username": username})
            if not empleados.correo_empleado == username and not empleados.contrasenia_empleado == password:
                messages.warning(request, 'usuario o contraseña incorrecto')
                return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def listarProductos():
    cursor = connection.cursor()
    cursor.execute("SELECT p.codigo_de_barras, p.nombre_producto, cat.nombre_categoria, i.cantidad_stock, det.precio, tp.nombre_tipo_precio, b.direccion_bodega, tpb.nombre_tipo_bodega, et.nombre_tipo, p.detalle_producto, p.direccion_foto_producto FROM producto p LEFT JOIN inventario i ON i.codigo_de_barras = p.codigo_de_barras LEFT JOIN categoria_producto cat ON cat.id_categoria = p.id_categoria LEFT JOIN detalle_precio_producto det ON det.codigo_de_barras = p.codigo_de_barras LEFT JOIN tipo_precio tp ON tp.id_tipo_precio = det.id_tipo_precio LEFT JOIN bodega b ON b.id_bodega = i.id_bodega LEFT JOIN tipo_bodega tpb ON tpb.id_tipo_bodega = b.id_tipo_bodega LEFT JOIN estado_producto et ON et.id_estado_producto = p.id_estado_producto WHERE p.activo =1 GROUP BY p.codigo_de_barras ORDER BY p.codigo_de_barras DESC")
    res = cursor.fetchall()
    cursor.close()
    return res


def addProduct(request):
    try:
        fs = FileSystemStorage(location='web/static/Uploads')
        cod = request.POST['codigoBarras']
        nombre = request.POST['nombreProducto']
        categoria = request.POST['categoria']
        estado = request.POST['estadoProducto']
        detalle = request.POST['detalle']
        file = request.FILES['file']
        bodega = request.POST['bodega']
        stock = request.POST['stock']
        pNormal = request.POST['pNormal']
        pOferta = request.POST['pOferta']
        pTarjeta = request.POST['pTarjeta']
        cursor = connection.cursor()
        cursor.execute('INSERT INTO `producto`(`codigo_de_barras`, `nombre_producto`, `id_categoria`, `id_estado_producto`, `detalle_producto`, `direccion_foto_producto`, `activo`) Values (%(cod)s, %(nombre)s,%(cat)s,%(est)s,%(det)s,%(file)s,1)', {'cod': cod, 'nombre': nombre, 'cat': categoria, 'est': estado, 'det': detalle, 'file': file.name})
        cursor.execute('INSERT INTO `inventario`(`codigo_de_barras`,`id_bodega`, `cantidad_stock`, `activo`)SELECT %(cod)s,%(bod)s,%(stock)s,1 FROM producto, bodega WHERE bodega.id_bodega= %(bod)s AND producto.codigo_de_barras = %(cod)s', {'cod': cod, 'bod':bodega, 'stock': stock})
        cursor.execute('INSERT INTO `detalle_precio_producto`( `codigo_de_barras`,`precio`, `id_tipo_precio`, `activo`) SELECT %(cod)s,%(pnormal)s,1,1 FROM producto WHERE producto.codigo_de_barras =%(cod)s', {'cod': cod, 'pnormal': pNormal})
        cursor.execute('INSERT INTO `detalle_precio_producto`( `codigo_de_barras`,`precio`, `id_tipo_precio`, `activo`) SELECT %(cod)s,%(poferta)s,2,1 FROM producto WHERE producto.codigo_de_barras = %(cod)s', {'cod': cod, 'poferta': pOferta})
        cursor.execute('INSERT INTO `detalle_precio_producto`( `codigo_de_barras`,`precio`, `id_tipo_precio`, `activo`) SELECT %(cod)s,%(ptarjeta)s,3,1 FROM producto WHERE producto.codigo_de_barras = %(cod)s', {'cod': cod, 'ptarjeta': pTarjeta})
        res = cursor.fetchall()
        fs.save(file.name, file)
        if len(res) == 0:
            messages.info(request, "Producto agregado exitosamente")
            return render(request, 'index.html')
        else:
            messages.warning(request, "No se puede agregar producto")
            return render(request, 'index.html')
    except Exception as e:
        messages.info(request, "Error "+e+"",)
        return render(request, 'index.html')


def delProducts(request):
    try:
        cod = request.POST['codigoBarras']
        cursor = connection.cursor()
        cursor.execute("UPDATE producto SET activo= 0 WHERE codigo_de_barras="+cod+"")
        res = cursor.fetchall()
        if len(res) == 0:
            cursor.close()
            messages.info(request, "Eliminado exitosamente")
            return render(request, 'index.html')
    except Exception as e:
        messages.info(request, "Error "+e+"",)
        return render(request, 'index.html')


def buscarProducto(request):
    codigo = request.POST['codigoBarras']
    cursor = connection.cursor()
    cursor.execute("SELECT p.codigo_de_barras, p.nombre_producto,cat.nombre_categoria, i.cantidad_stock, det.precio, tp.nombre_tipo_precio, b.direccion_bodega, tpb.nombre_tipo_bodega, et.nombre_tipo, p.detalle_producto, p.direccion_foto_producto, p.activo FROM producto p LEFT JOIN inventario i on i.codigo_de_barras=p.codigo_de_barras LEFT JOIN categoria_producto cat on cat.id_categoria=p.id_categoria LEFT JOIN detalle_precio_producto det on det.codigo_de_barras=p.codigo_de_barras LEFT JOIN tipo_precio tp on tp.id_tipo_precio=det.id_tipo_precio LEFT JOIN bodega b on b.id_bodega=i.id_bodega LEFT JOIN tipo_bodega tpb on tpb.id_tipo_bodega=b.id_tipo_bodega LEFT JOIN estado_producto et on et.id_estado_producto=p.id_estado_producto WHERE p.codigo_de_barras="+codigo+"  GROUP BY p.codigo_de_barras")
    context = {
        "productos": cursor.fetchall()
    }
    cursor.close()
    return render(request, 'buscar.html', context)


def buscarProductoModificar(request):
    codigo = request.POST['codigoBarras']
    cursor = connection.cursor()
    cursor.execute("SELECT p.codigo_de_barras, p.nombre_producto,cat.nombre_categoria, i.cantidad_stock, det.precio, tp.nombre_tipo_precio, b.direccion_bodega, tpb.nombre_tipo_bodega, et.nombre_tipo, p.detalle_producto, p.direccion_foto_producto, p.activo FROM producto p LEFT JOIN inventario i on i.codigo_de_barras=p.codigo_de_barras LEFT JOIN categoria_producto cat on cat.id_categoria=p.id_categoria LEFT JOIN detalle_precio_producto det on det.codigo_de_barras=p.codigo_de_barras LEFT JOIN tipo_precio tp on tp.id_tipo_precio=det.id_tipo_precio LEFT JOIN bodega b on b.id_bodega=i.id_bodega LEFT JOIN tipo_bodega tpb on tpb.id_tipo_bodega=b.id_tipo_bodega LEFT JOIN estado_producto et on et.id_estado_producto=p.id_estado_producto WHERE p.codigo_de_barras="+codigo+"  GROUP BY p.codigo_de_barras")
    context = {
        'ListaC': CategoriaProducto.objects.all(),
        'ListaE': EstadoProducto.objects.all(),
        'listaB': Bodega.objects.all(),
        'listaD': DetallePrecioProducto.objects.all(),
        "productos": cursor.fetchall()
    }
    cursor.close()
    return render(request, 'modificar.html', context)


def addProduct(request):
    try:
        fs = FileSystemStorage(location='web/static/Uploads')
        cod = request.POST['codigoBarras']
        nombre = request.POST['nombreProducto']
        categoria = request.POST['categoria']
        estado = request.POST['estadoProducto']
        detalle = request.POST['detalle']
        file = request.FILES['file']
        bodega = request.POST['bodega']
        stock = request.POST['stock']
        pNormal = request.POST['pNormal']
        pOferta = request.POST['pOferta']
        pTarjeta = request.POST['pTarjeta']
        cursor = connection.cursor()
        cursor.execute('INSERT INTO `producto`(`codigo_de_barras`, `nombre_producto`, `id_categoria`, `id_estado_producto`, `detalle_producto`, `direccion_foto_producto`, `activo`) Values (%(cod)s, %(nombre)s,%(cat)s,%(est)s,%(det)s,%(file)s,1)', {'cod': cod, 'nombre': nombre, 'cat': categoria, 'est': estado, 'det': detalle, 'file': file.name})
        cursor.execute('INSERT INTO `inventario`(`codigo_de_barras`,`id_bodega`, `cantidad_stock`, `activo`)SELECT %(cod)s,%(bod)s,%(stock)s,1 FROM producto, bodega WHERE bodega.id_bodega= %(bod)s AND producto.codigo_de_barras = %(cod)s', {'cod': cod, 'bod':bodega, 'stock': stock})
        cursor.execute('INSERT INTO `detalle_precio_producto`( `codigo_de_barras`,`precio`, `id_tipo_precio`, `activo`) SELECT %(cod)s,%(pnormal)s,1,1 FROM producto WHERE producto.codigo_de_barras =%(cod)s', {'cod': cod, 'pnormal': pNormal})
        cursor.execute('INSERT INTO `detalle_precio_producto`( `codigo_de_barras`,`precio`, `id_tipo_precio`, `activo`) SELECT %(cod)s,%(poferta)s,2,1 FROM producto WHERE producto.codigo_de_barras = %(cod)s', {'cod': cod, 'poferta': pOferta})
        cursor.execute('INSERT INTO `detalle_precio_producto`( `codigo_de_barras`,`precio`, `id_tipo_precio`, `activo`) SELECT %(cod)s,%(ptarjeta)s,3,1 FROM producto WHERE producto.codigo_de_barras = %(cod)s', {'cod': cod, 'ptarjeta': pTarjeta})
        res = cursor.fetchall()
        fs.save(file.name, file)
        if len(res) == 0:
            messages.info(request, "Producto agregado exitosamente")
            return render(request, 'index.html')
        else:
            messages.warning(request, "No se puede agregar producto")
            return render(request, 'index.html')
    except Exception as e:
        messages.info(request, "Error "+e+"",)
        return render(request, 'index.html')
