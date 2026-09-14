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

## CI/CD

**CI** (`.github/workflows/ci.yml`) runs on every push to `main` and every pull
request: installs dependencies, fails if you forgot a migration
(`makemigrations --check`), runs Django's system checks, then runs the test
suite (`todos/tests.py`). Watch it in the repo's **Actions** tab.

**CD** (`.github/workflows/cd.yml`) runs on every push to `main`: builds the
`Dockerfile` and publishes the image to GitHub Container Registry, tagged
`latest` plus the commit SHA:

```
ghcr.io/ankitjawla/django-todo:latest
```

Run the shipped image anywhere Docker runs:

```bash
docker run -p 8000:8000 \
  -e DJANGO_SECRET_KEY='some-long-random-value' \
  ghcr.io/ankitjawla/django-todo:latest
```

The container runs migrations on startup and serves with gunicorn;
WhiteNoise serves static files so no nginx is needed. For production, also set
`DJANGO_DEBUG=False` (already the default in the image) and
`DJANGO_ALLOWED_HOSTS=yourdomain.com`.

## What's inside

- `todos/models.py` — the `Task` model (title, completed, created_at)
- `todos/views.py` — list/add, toggle, delete views
- `todos/urls.py` — URL routes for the app
- `todos/templates/todos/task_list.html` — the page
- `todos/admin.py` — Task in the Django admin
