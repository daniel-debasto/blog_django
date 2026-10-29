# Blog Django
Proyecto base de un blog web desarrollado con Django.

## Descripción
Este repositorio contiene la estructura inicial de un proyecto Django para construir un blog. Incluye la configuración base del proyecto y una aplicación llamada `posts`.

## Instalación
Clonar el repositorio:
```bash
git clone URL_DEL_REPOSITORIO
```

Entrar a la carpeta del proyecto:
```bash
cd NOMBRE_DEL_REPOSITORIO
```

Crear entorno virtual:
```bash
python -m venv env
```

Activar entorno virtual (En Windows PowerShell):
```bash
.\env\Scripts\Activate.ps1
```

Instalar dependencias:
```bash
pip install -r requirements.txt
```

Ejecutar el servidor:
```bash
python manage.py runserver
```

Abrir en el navegador: http://127.0.0

## Aplicaciones
* **posts**: aplicación inicial para manejar las publicaciones del blog.


## Módulo 10: CRUD de Posts con Imágenes

### Dependencias instaladas
* **Pillow**: Necesario para el procesamiento y validación de campos `ImageField` en Django.

### Configuración del manejo de imágenes
1. Se añadió el campo `imagen` al modelo `Post` usando `models.ImageField(upload_to='posts/', null=True, blank=True)`.
2. Se configuraron las variables `MEDIA_URL` y `MEDIA_ROOT` en `settings.py`.
3. Se modificó el archivo `urls.py` principal para servir archivos multimedia en el entorno de desarrollo local mediante `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`.
4. Se incorporó el atributo `enctype="multipart/form-data"` en el formulario HTML para habilitar el envío seguro de archivos binarios al servidor.

### Operaciones CRUD disponibles
* **Listar**: En la página principal del blog (`/`).
* **Detalle**: Detalle individual del post con su correspondiente imagen adjunta (`/post/<id>/`).
* **Crear**: Formulario dinámico con soporte de carga multimedia (`/post/crear/`).
* **Editar**: Actualización de textos y reemplazo o carga de imágenes (`/post/<id>/editar/`).
* **Eliminar**: Remoción lógica y física mediante pantalla de confirmación interactiva (`/post/<id>/eliminar/`).

### Cómo probar la carga de imágenes
1. Iniciar el servidor: `python manage.py runserver`.
2. Dirigirse al navegador a la ruta de creación (`/post/crear/`).
3. Completar los campos y subir un archivo de prueba (.png o .jpg) en el campo de imagen.
4. Guardar y verificar que se visualice correctamente en la vista de detalle.

