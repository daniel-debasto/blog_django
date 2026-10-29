# CORRECCIÓN EN LA LÍNEA 1:
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# 1. READ - Listar todos los posts
def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/lista_posts.html', {'posts': posts})

# 2. READ - Ver el detalle de un post individual
def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/detalle_post.html', {'post': post})

# 3. CREATE - Crear un nuevo post con imagen
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) # ¡Crucial para las imágenes!
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form, 'accion': 'Crear'})

# 4. UPDATE - Editar un post existente y cambiar imagen
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form, 'accion': 'Editar'})

# 5. DELETE - Eliminar un post mediante confirmación previa
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})
