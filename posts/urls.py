from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_inicio, name='inicio'),
    path('acerca/', views.vista_acerca, name='acerca'),
]
