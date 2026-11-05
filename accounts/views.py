from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroForm, PerfilForm
from .models import Perfil

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # 1. Guarda al usuario en la base de datos
            usuario = form.save() 
            
            # 2. REQUISITO EXPLÍCITO: Crea el objeto Perfil usando la variable del usuario recién guardado
            Perfil.objects.create(user=usuario)
            
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}! Ya podés iniciar sesión.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'accounts/registro.html', {'form': form})

@login_required
def ver_perfil(request):
    return render(request, 'accounts/perfil.html')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        # request.FILES procesa correctamente las imágenes del avatar
        form = PerfilForm(request.POST, request.FILES, instance=request.user.perfil)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado con éxito!')
            return redirect('ver_perfil')
    else:
        form = PerfilForm(instance=request.user.perfil)
    return render(request, 'accounts/editar_perfil.html', {'form': form})
