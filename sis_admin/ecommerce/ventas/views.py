from django.shortcuts import render
from django.shortcuts import HttpResponse

html_base = """
        <h1> Shopping Car </h1>
        <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/articulo">Articulos</a></li>
            <li><a href="/cliente">Clientes</a></li>
            <li><a href="/venta">Ventas</a></li>
            <li><a href="/consulta">Consultas</a></li>
        </ul>          
        """


def inicio(request):
    data = {
        'titulo':"Inicio"
    }
    return render(request,'base.html',data)

def articulo(request):
    return HttpResponse(html_base+
                        """<h2>Mantenimiento de Articulo<h2>
                        <p>Lista de articulos</p>""")

def cliente(request):
    data = {
        'titulo':'GESTION DE CLIENTES',
        'crear_url':'/crearcliente',
        'lista_url':'/cliente',
    }
    return render(request, "ventas/clientes/listCliente.html",data)

def crearCliente(request):
    data = {
        'titulo':'Mantenimiento de Clientes',
        'crear_url':'/crearcliente',
        'action':'add',
        'listar_url':'/cliente',
    }
    return render(request, "ventas/clientes/formCliente.html",data)

def venta (request):
    data = {
        'titulo':"Inicio"
    }
    return render(request, "ventas/ventas.html",data)

#def compra (request):
    #data ={
        #'titulo':"Inicio"
    #}
    #return render(request, "compras/compras.html",data)