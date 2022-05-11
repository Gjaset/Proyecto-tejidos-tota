from django.shortcuts import render, redirect
from facturas.models import Factura
from facturas.forms import FacturaForm
from django.contrib import messages 


def factura(request):
    facturadb = Factura.objects.all()
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'!La factura se agregó correctamente!')
            return redirect('factura-factura')
    else:
        form = FacturaForm()
    return render(request,'factura/crearFactura.html', ({'base_datos':facturadb,'form':form}))

def tfactura(request):
    tfacturas= Factura.objects.all()
    context={
        "tfacturas": tfacturas,
    }
    return render(request, "factura/factura.html",context)


def vfactura (request,pk):
    titulo_pagina="Factura"
    factura= Factura.objects.get(id=pk)
    print(factura)
    context={
        "factura": factura,
        "titulo_pagina":titulo_pagina
    }
    return render(request,"factura/verfactura.html", context)

# Create your views here.
