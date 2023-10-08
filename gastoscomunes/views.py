from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def gastoscomunes(request):
    return render(request, 'gastoscomunes.html')

def contacto(request):
    return render(request, 'contacto.html')