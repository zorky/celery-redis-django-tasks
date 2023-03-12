import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

app = Celery("tasks")
app.config_from_object("core.async_tasks.celery_config")

# par défaut, il recherche les tâches dans le module "tasks.py" https://docs.celeryq.dev/en/stable/reference/celery.html#celery.Celery.autodiscover_tasks
app.autodiscover_tasks(['api'])
