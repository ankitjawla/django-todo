# Django Todo — a tiny learning project

A minimal todo app built with Django: add tasks, mark them done, delete them.
Includes the Django admin for free.

## Run it

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser   # optional, for /admin
python manage.py runserver
```

Open http://127.0.0.1:8000/ — the admin lives at http://127.0.0.1:8000/admin/.

## What's inside

- `todos/models.py` — the `Task` model (title, completed, created_at)
- `todos/views.py` — list/add, toggle, delete views
- `todos/urls.py` — URL routes for the app
- `todos/templates/todos/task_list.html` — the page
- `todos/admin.py` — Task in the Django admin
