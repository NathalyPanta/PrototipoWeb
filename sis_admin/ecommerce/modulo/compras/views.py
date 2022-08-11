from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def compra(request):
    data ={
        'titulo':"Inicio"
    }
    return render(request, "compras/compra.html",data)

def proveedor(request):
    data = {
        'titulo':'GESTION DE PROVEEDORES',
        'crearP_url':'/crearprov',
        'listaP_url':'/proveedor',
    }
    return render(request, "compras/op/proveedor.html",data)

def crearProveedor(request):
    data = {
        'titulo':'Mantenimiento de Proveedores',
        'crear_P_url':'/crearprov',
        'action':'add',
        'listaP_url':'/proveedor',
    }
    return render(request, "compras/op/formprov.html",data)

def listadoCompra(request):
    data = {
        'titulo':'Lista de Compras',
        'aggCompra_url':'/aggcompra',
        'action':'add',
        'listaCompra_url':'listacompra',
    }
    return render(request, "compras/op/listado.html",data)

def registroCompra(request):
    data ={
        'titulo':'Registro de Compras',
    }
    return render(request, "compras/op/registro.html",data)

def pedido(request):
    data ={
        'titulo':'Pedidos'
    }
    return render(request, "compras/op/lis_ped.html",data)

def re_pedido(request):
    data={
        'titulo':'Registrar Pedido',
        'RegistraP_url':'pedido'
    }
    return render (request, "compras/op/pedido.html",data)