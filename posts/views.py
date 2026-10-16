from django.shortcuts import render

def vista_inicio(request):
    return render(request, 'posts/inicio.html')

def vista_acerca(request):
    return render(request, 'posts/acerca.html')
