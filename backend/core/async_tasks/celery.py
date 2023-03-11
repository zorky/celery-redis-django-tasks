import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

app = Celery("tasks")
app.config_from_object("core.async_tasks.celery_config")
# app.config_from_object("api_core.async_tasks.async_tasks")

# autodiscover_tasks cherche dans une liste de packages (paramètre packages),
# le module task.py (ou le paramètre related_name)
# packages=['tasks'], related_name='sample' revient à import tasks.sample
# Exemple:
# app.autodiscover_tasks(packages=['api_core.async_tasks'], related_name='sample')

# Comme DJANGO_SETTINGS_MODULE est défini, autodiscover_tasks sans paramètre
# recherche dans les packages django le module tasks.py
# Exemple: api_rdv_cmp/tasks.py
app.autodiscover_tasks(['api'])
