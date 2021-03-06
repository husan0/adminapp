"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from web.views import *

urlpatterns = [
    #carga
    url(r'^$', login, name='login'),
    url(r'^index', index, name='index'),
    url(r'^logout', logout, name='logout'),
    url(r'^add', add, name='add'),
    url(r'^list', list, name='list'),
    url(r'^search', search, name='search'),
    url(r'^update', update, name='update'),
    url(r'^delete', delete, name='delete'),
    #ejecucion
    url(r'^agregar', addProduct, name='agregar'),
    url(r'^eliminar', delProducts, name='eliminar'),
    url(r'^buscar', buscarProducto, name='buscar'),
    url(r'^modificar', buscarProductoModificar, name='buscarmodificar'),
]
