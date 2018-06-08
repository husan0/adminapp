from django.shortcuts import render
from django.contrib import messages
from django.template import RequestContext

from .models import *


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        if username and password is not None:
            empleado = Empleado.objects.all()
            for empleado in empleado:
                if empleado.correo_empleado == username and empleado.contrasenia_empleado == password:
                    request.COOKIES['user'] = username
                    return render(request, 'index.html', {"username": username})
        else:
            messages.warning(request, 'Usuario o contraseña incorrecto')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def index(request):
    if request.GET != '':
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')


def logout(request):
    request.COOKIES['user'] = ''
    messages.warning(request, 'Desconectado exitosamente')
    return render(request, 'login.html')


def add(request):
    if request.GET != '':
        contexts = {
            'ListaC': CategoriaProducto.objects.all(),
            'ListaE': EstadoProducto.objects.all(),
            'listaB': Bodega.objects.all(),
        }
        return render(request, 'agregar.html', contexts)
    else:
        return render(request, 'login.html')


def addProduct(request):
    cod = request.POST.get('codigoBarras')
    nombre = request.POST.get('nombreProducto')
    categoria = request.POST.get('categoria')
    estado = request.POST.get('estadoProducto')
    detalle = request.POST.get('detalle')
    file = request.POST.get('file')
    bodega = request.POST.get('bodega')
    stock = request.POST.get('stock')
    pNormal = request.POST.get('pNormal')
    pOferta = request.POST.get('pOferta')
    pTarjeta = request.POST.get('pTarjeta')
    producto = Producto.objects.aggregate(cod,nombre,categoria,estado,detalle,
                                          file,bodega,stock,pNormal,pOferta,pTarjeta,1)
    if producto.save():
        messages.info("Producto agregado exitosamente")
        return render(request, 'index.html')
    else:
        messages.warning("No se pudo agregar")
        return render(request, 'index.html')


def search(request):
    if request.GET != '':
        return render(request, 'buscar.html')
    else:
        return render(request, 'login.html')


def delete(request):
    if request.GET != '':
        return render(request, 'eliminar.html')
    else:
        return render(request, 'login.html')


def list(request):
    if request.GET != '':
        return render(request, 'listar.html')
    else:
        return render(request, 'login.html')


def update(request):
    if request.GET != '':
        return render(request, 'modificar.html')
    else:
        return render(request, 'login.html')
