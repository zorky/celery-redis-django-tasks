import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

app = Celery("tasks")
app.config_from_object("core.async_tasks.celery_config")

app.autodiscover_tasks(['api'])
