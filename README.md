# Blog Django - Proyecto Final Python

Este es el proyecto consolidado para la entrega final del módulo de Python y Django. Consiste en un blog web completamente funcional que integra la gestión de publicaciones con paginación, carga de imágenes, autenticación de usuarios, perfiles personalizados y sección informativa.

## 🚀 Funcionalidades Principales

### 📝 Gestión de Posts (CRUD Completo) y Navegación
* **Listar y Paginación:** Visualización de las publicaciones en tarjetas limpias con extracto de texto y paginación dinámica (`Paginator`) en la página principal.
* **Detalle:** Vista individual para cada post con su contenido completo e imagen adjunta.
* **Crear:** Formulario dinámico con soporte de carga multimedia y asignación automática del autor según el usuario conectado.
* **Editar:** Modificación de textos y reemplazo o carga de imágenes.
* **Eliminar:** Remoción de publicaciones mediante pantalla de confirmación interactiva.
* **Sección Acerca de:** Página dedicada con información sobre el propósito del blog y su desarrollo.

### 🔐 Sistema de Autenticación y Perfiles
* **Autenticación Completa:** Inicio y cierre de sesión de usuarios mediante el sistema nativo de Django.
* **Registro Personalizado:** Formulario de alta para nuevos usuarios con validación obligatoria de correo electrónico.
* **Extensión del Modelo (Perfil):** Modelo `Perfil` vinculado a `User` que incluye biografía, avatar (imagen) y enlace web.
* **Creación Automática:** Generación automática del perfil en la base de datos inmediatamente después de registrarse un usuario.
* **Protección de Rutas:** Restricción de acceso mediante decoradores (`@login_required`) y validación en plantillas para asegurar que los visitantes anónimos no puedan crear, editar ni borrar publicaciones.

---

## 🛠️ Tecnologías Utilizadas

* **Python 3**
* **Django 6**
* **Pillow** (Procesamiento y validación de imágenes)
* **SQLite** (Base de datos local)
* **HTML5 / CSS3** (Estilos personalizados e interfaz web responsiva)

---

## 🔧 Instrucciones de Instalación y Ejecución

Seguí estos pasos para clonar el repositorio, reconstruir el entorno y ejecutar el proyecto desde cero localmente:

### 1. Clonar el repositorio
```bash
git clone https://github.com/daniel-debasto/blog_django.git
cd blog_django
```

### 2. Crear y activar el entorno virtual
* **En Windows (PowerShell):**
  ```bash
  python -m venv env
  ./env/Scripts/Activate.ps1
  ```
* **En macOS/Linux:**
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```

### 3. Instalar las dependencias
Con el entorno virtual activo, instalá los paquetes necesarios detallados en el archivo de requerimientos:
```bash
pip install -r requirements.txt
```

### 4. Ejecutar las migraciones
Creá la estructura de las tablas en tu base de datos local:
```bash
python manage.py makemigrations accounts
python manage.py makemigrations posts
python manage.py migrate
```

### 5. Crear un Superusuario (Administrador)
Para gestionar el panel administrativo de Django o realizar pruebas globales con un rol de administrador, ejecutá el siguiente comando y completá los datos (usuario, email y contraseña):
```bash
python manage.py createsuperuser
```

### 6. Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```

Una vez iniciado, abrí tu navegador e ingresá a: `http://127.0.0`

---

## 👤 Autor

* **Daniel Debasto**
