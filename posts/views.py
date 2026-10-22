from django.shortcuts import render
from .models import Post

def vista_inicio(request):
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    return render(request, "posts/inicio.html", {"posts": posts})

def lista_posts(request):
    # Código exacto requerido por la consigna:
    posts = Post.objects.filter(estado="publicado").order_by("-fecha_creacion")
    context = {
        "posts": posts
    }
    return render(request, "posts/lista_posts.html", context)

def vista_acerca(request):
    return render(request, "posts/acerca.html")
