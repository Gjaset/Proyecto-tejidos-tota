from django.shortcuts import render, redirect
from usuarios.forms import    UsuarioForm
from usuarios.models import  Usuario
from django.contrib import messages 


def cusuario(request):
    titulo_pagina="usuario"
    usuario_db = Usuario.objects.all()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            usuario_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El usuario {usuario_nombre} se agregó correctamente!')
            return redirect('usuario-crearUsuario')
    else:
        form = UsuarioForm()
    return render(request,'usuario/crearUsuario.html', ({'base_datos':usuario_db,'form':form, "titulo_pagina":titulo_pagina}))

def tusuario(request):
    titulo_pagina="usuario"
    tusuarios= Usuario.objects.all()
    context={
        "tusuarios": tusuarios,
        "titulo_pagina":titulo_pagina
    }
    return render(request, "usuario/tablaUsuario.html",context)

def vusuario (request,pk):
    titulo_pagina="Producto"
    usuario= Usuario.objects.get(id=pk) 
    print(usuario)
    context={
        "usuario": usuario,
        "titulo_pagina":titulo_pagina
    }
    return render(request,"usuario/verusuario.html", context)


def Editarusuario(request,pk):
    titulo_pagina="usuario"
    usuario_db = Usuario.objects.get(id=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario_db)
        if form.is_valid():
            form.save()
        
        return redirect('usuario-tablaUsuario')
    else:
        form = UsuarioForm(instance=usuario_db)
        context={
        "cusuario": cusuario,
        "titulo_pagina":titulo_pagina
    }
    return render(request,'usuario/editarusuario.html', ({'base_datos':usuario_db,'form':form,"titulo_pagina":titulo_pagina}))

