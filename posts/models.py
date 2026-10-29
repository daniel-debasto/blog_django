from django.db import models

class Post(models.Model):
    # Definimos las opciones predefinidas para el estado del post (Borrador, Publicado, Archivado)
    ESTADO_CHOICES = [
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
        ('archivado', 'Archivado'),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título")
    contenido = models.TextField(verbose_name="Contenido")
    autor = models.CharField(max_length=100, verbose_name="Autor")
    
    # auto_now_add=True guarda automáticamente la fecha y hora al crear el registro
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    
    # Campo estado mapeado a nuestras opciones predefinidas
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='borrador',
        verbose_name="Estado"
    )
    imagen = models.ImageField(upload_to='posts/', null=True, blank=True)


    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    # El método __str__ permite identificar al post por su título en el panel de administración
    def __str__(self):
        return self.titulo
