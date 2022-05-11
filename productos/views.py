from django.shortcuts import render, redirect
from productos.forms import TallaForm,MarcaForm, ColorForm, ProductoForm
from productos.models import Talla, Marca, Color, Producto
from django.contrib import messages

def talla(request):
    titulo_pagina="Productos"
    tallas= Talla.objects.all()
    if request.method == 'POST':
        form= TallaForm(request.POST)
        if form.is_valid():
            form.save()
            nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'La talla {nombre} se agregó correctamente!')
            return redirect('producto-talla')
        else:
            nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'La talla {nombre} no se ha podido agregar!')

            return redirect('producto-talla')
    else:
        form= TallaForm()
    context={
        "titulo_pagina": titulo_pagina,
        "tallas": tallas,
        "form":form
    }
    return render(request, "producto/creartalla.html", context)
def marca(request):
    titulo_pagina="Productos"
    marcas= Marca.objects.all()
    if request.method == 'POST':
        form= MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            marca_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'La marca {marca_nombre} se agregó correctamente!')
        return redirect('producto-marca')
    else:
        form = MarcaForm()
    context={
        "titulo_pagina": titulo_pagina,
        "marcas": marcas,
        "form":form
    }
    return render(request, "producto/crearmarca.html", context)

def color(request):
    colores= Color.objects.all()
    if request.method == 'POST':
        form= ColorForm(request.POST)
        if form.is_valid():
            form.save()
            color_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'La color {color_nombre} se agregó correctamente!')
        return redirect('producto-color')
    else:
        form = ColorForm()
    context={
        "colores": colores,
        "form":form
    }
    return render(request, "producto/color.html", context)


def producto(request):
    titulo_pagina="Producto"
    productt = Producto.objects.all()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            producto_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El producto {producto_nombre} se agregó correctamente!')
        return redirect('producto-producto')
    else:
        form = ProductoForm()
    return render(request,'producto/crearproducto.html', ({'base_datos':productt,'form':form,  "titulo_pagina":titulo_pagina}))


def productoT (request):
    titulo_pagina="Producto"
    productoTs= Producto.objects.all() 
    context={
        "productoTs": productoTs,
        "titulo_pagina":titulo_pagina
    }
    return render(request,"producto/producto.html", context)

def Verproducto (request,pk):
    titulo_pagina="Producto"
    producto= Producto.objects.get(id=pk) 
    print(producto)
    context={
        "producto": producto,
        "titulo_pagina":titulo_pagina
    }
    return render(request,"producto/verproducto.html", context)


def Editarproducto(request,pk):
    titulo_pagina="Producto"
    productt = Producto.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=productt)
        if form.is_valid():
            form.save()
        
        return redirect('producto-producto')
    else:
        form = ProductoForm(instance=productt)
        context={
        "producto": producto,
        "titulo_pagina":titulo_pagina
    }
    return render(request,'producto/editarproducto.html', ({'base_datos':productt,'form':form,  "titulo_pagina":titulo_pagina}))


def Editartalla(request,pk):
    titulo_pagina="Producto"
    tallas= Talla.objects.get(id=pk)
    if request.method == 'POST':
        form= TallaForm(request.POST, instance=tallas)
        if form.is_valid():
            form.save()
        return redirect('producto-talla')
    else:
        form= TallaForm(instance=tallas)
        context={
        "tallas": tallas,
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "producto/editartalla.html", ({'base_datos':tallas,'form':form,  "titulo_pagina":titulo_pagina}))

def Editarmarca(request,pk):
    titulo_pagina="Producto"
    marcas= Marca.objects.get(id=pk)
    if request.method == 'POST':
        form= MarcaForm(request.POST, instance=marcas)
        if form.is_valid():
            form.save()
        return redirect('producto-marca')
    else:
        form= MarcaForm(instance=marcas)
        context={
        "marcas": marcas,
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "producto/editarmarca.html", ({'base_datos':marcas,'form':form,  "titulo_pagina":titulo_pagina}))



















