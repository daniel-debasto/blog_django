from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Esto cumple con el requisito de mostrar columnas útiles en el listado
    list_display = ('titulo', 'autor', 'estado', 'fecha_creacion')
    
    # Agrega filtros laterales para buscar por estado o fecha (muy útil en blogs)
    list_filter = ('estado', 'fecha_creacion')
    
    # Permite buscar posts por título o contenido desde una barra de búsqueda
    search_fields = ('titulo', 'contenido')
