# Carta Digital Backend

This project is based on React and Django: It creates a digital menu for restaurants (UDEMY - Agustin Navarro Galdon). It has modifications due to having a different folder and file structure, using other dependencies, and managing applications.

## How to Start the Project

1. Run `pip install -r requirements_windows.txt` for Windows or `pip install -r requirements_linux.txt` for Linux to install the required dependencies.
2. Execute `python manage.py makemigrations` followed by `python manage.py migrate` to apply database migrations.
3. Populate superusers using `python manage.py fill_superusers`.
4. Start the development server with `python manage.py runserver`.

## Custom Commands

1. **Delete Migrations:**
   - `python manage.py delete_migrations`: Deletes all migrations in the 'apps' folder, excluding \_\_init\_\_.py'.
   - Options:
     - `-sp NOMBRE_APP` or `--skippermanent NOMBRE_APP`: Adds the app name to a txt file, skipping permanent deletion.
     - `-s NOMBRE_APP` or `--skip NOMBRE_APP`: Skips deleting migrations for the specified app only in the current execution.

2. **Fill Superusers:**
   - `python manage.py fill_superusers.py`: Creates, deletes, adds, or removes super users.
   - Options:
     - `--add`, `--addcreate`, `--delete`, `--deleteremove`: Modify the super user list in the JSON file.
       - `add`/`delete`: Adds/Deletes the super user from the JSON file.
       - `addcreate`/`deleteremove`: Adds/Deletes the super user from the JSON file and creates/deletes it in the DB.

## Project Structure

```cmd
\---backend
    |   .gitignore
    |   manage.py
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
