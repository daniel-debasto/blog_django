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

## ## Módulo 11: Sistema de Autenticación y Perfiles

### ### Nuevas Características Implementadas
1. **Autenticación Completa:** Se integró el sistema nativo de Django (`django.contrib.auth`) para resolver de manera robusta el **Login** y **Logout** de usuarios. El cierre de sesión se ejecuta mediante un formulario con método `POST` asegurando compatibilidad total.
2. **Formulario de Registro Personalizado:** Se desarrolló `RegistroForm` extendiendo de `UserCreationForm` para dar de alta nuevos usuarios incorporando de manera obligatoria la validación del correo electrónico.
3. **Extensión del Modelo (Perfil):** Se creó el modelo `Perfil` con una relación estricta `OneToOneField` vinculada a `User`. Incluye los campos requeridos: `biografia` (`TextField`), `avatar` (`ImageField`) y `link_web` (`URLField` opcional).
4. **Creación Automática del Perfil:** El objeto se instancia de manera directa y segura en la base de datos desde la vista de registro inmediatamente después de guardar al usuario, usando:
   ```python
   Perfil.objects.create(user=usuario)
   ```
5. **Protección de Rutas:** Se aplicó el decorador `@login_required` para bloquear el acceso directo por URL a las funciones de creación, edición y borrado de posts si un visitante es anónimo. Las vistas de listado y detalle siguen siendo públicas.
6. **Navegación Dinámica:** La barra de menú en `base.html` valida el estado del usuario mediante `{% if user.is_authenticated %}` para alternar las opciones de gestión visibles en tiempo real.

### ### Cómo probar las nuevas funcionalidades
1. **Migraciones:** Ejecutar los comandos de base de datos para crear la tabla de perfiles:
   ```bash
   python manage.py makemigrations accounts
   python manage.py migrate
   ```
2. **Registro:** Ingresar a `/accounts/registro/` para dar de alta un nuevo usuario.
3. **Verificación:** Iniciar sesión en `/accounts/login/` y validar que ahora es posible visualizar el menú extendido y acceder a la creación de publicaciones.


