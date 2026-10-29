from django.urls import path
from . import views

urlpatterns = [
    # Rutas anteriores de tu proyecto (para que funcione el menú de base.html)
    path('', views.lista_posts, name='inicio'),
    path('lista/', views.lista_posts, name='lista_posts'),
    path('acerca/', views.lista_posts, name='acerca'), # Apunta temporalmente aquí para que no rompa
    
    # Rutas del CRUD
    path('post/<int:pk>/', views.detalle_post, name='detalle_post'),
    path('post/crear/', views.crear_post, name='crear_post'),
    path('post/<int:pk>/editar/', views.editar_post, name='editar_post'),
    path('post/<int:pk>/eliminar/', views.eliminar_post, name='eliminar_post'),
]
