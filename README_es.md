# Carta Digital Backend

Este proyecto toma como base React y Django: Crea una carta digital para restaurantes (UDEMY - Agustin Navarro Galdon).
Tiene modificaciones al tener una estructura de carpetas y archivos diferentes, utilizar otras dependencias y manejo de aplicaciones

## Cómo Iniciar el Proyecto

1. Ejecuta `pip install -r requirements_windows.txt` en Windows o `pip install -r requirements_linux.txt` en Linux para instalar las dependencias necesarias.
2. Ejecuta `python manage.py makemigrations` seguido de `python manage.py migrate` para aplicar las migraciones de la base de datos.
3. Llena los superusuarios con `python manage.py fill_superusers`.
4. Inicia el servidor de desarrollo con `python manage.py runserver`.

## Comandos Personalizados

1. **Eliminar Migraciones:**
   - `python manage.py delete_migrations`: Elimina todas las migraciones en la carpeta 'apps', excluyendo \_\_init\_\_.py'.
   - Opciones:
     - `-sp NOMBRE_APP` o `--skippermanent NOMBRE_APP`: Agrega el nombre de la aplicación a un archivo txt, evitando la eliminación permanente.
     - `-s NOMBRE_APP` o `--skip NOMBRE_APP`: Evita que se eliminen las migraciones solo en esa ejecución.

2. **Llenar Superusuarios:**
   - `python manage.py fill_superusers.py`: Crea, elimina, agrega o elimina superusuarios.
   - Opciones:
     - `--add`, `--addcreate`, `--delete`, `--deleteremove`: Modifica la lista de superusuarios en el archivo JSON.
       - `add`/`delete`: Agrega/Elimina el superusuario del archivo JSON.
       - `addcreate`/`deleteremove`: Agrega/Elimina el superusuario del archivo JSON y lo crea/elimina en la base de datos.

## Estructura del Proyecto

```cmd
\---backend
    |   .gitignore
    |   manage.py
    |   README_es.md
    |   README.md
    |   requirements_linux.txt
    |   requirements_windows.txt
    |   stderr.log
    |
    +---apps
    |   +---users
    |   |   |   admin.py
    |   |   |   apps.py
    |   |   |   models.py
    |   |   |   tests.py
    |   |   |   views.py
    |   |   |   __init__.py
    |   |   |
    |   |   \---migrations
    |   |           __init__.py
    |   |
    |   \---utils
    |       |   admin.py
    |       |   apps.py
    |       |   models.py
    |       |   tests.py
    |       |   views.py
    |       |   __init__.py
    |       |
    |       +---api
    |       |       __init__.py
    |       |
    |       +---backend
    |       |       __init__.py
    |       |
    |       +---context_processors
    |       |       __init__.py
    |       |
    |       +---data
    |       |       skip_apps.txt
    |       |       super_users.json
    |       |
    |       +---management
    |       |   |   __init__.py
    |       |   |
    |       |   \---commands
    |       |           delete_migrations.py
    |       |           fill_superusers.py
    |       |           __init__.py
    |       |
    |       +---migrations
    |       |       0001_add_unnacent_and_trigram.py
    |       |       __init__.py
    |       |
    |       \---templates
    |               errors_template.html
    |
    +---app_core
    |       asgi.py
    |       settings.py
    |       urls.py
    |       wsgi.py
    |       __init__.py
```
