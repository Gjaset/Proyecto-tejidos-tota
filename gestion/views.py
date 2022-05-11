from django.shortcuts import redirect,render


def index(request):
    
    titulo_pagina="Index"
    context={
        'titulo_pagina':titulo_pagina
    }
    return render(request,'index.html',context)
def inicio(request):
    
    titulo_pagina="Inicio"
    context={
        'titulo_pagina':titulo_pagina
    }
    return render(request,'inicio.html',context)