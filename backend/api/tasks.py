from time import sleep
import logging
logger = logging.getLogger('django')
# from celery import shared_task
from core.async_tasks.celery import app

# OperationalError
# [Errno 111] Connection refused
# @shared_task()

@app.task
def execute_long_task(title: str, delay: int, wordings: list):
    logger.info(f"** On s'endort {delay} secondes avant de lancer la tâche ZZzzzZZzzzzzzzzz **")

    sleep(delay)

    logger.info(f'** On se réveille ! Démarrage de la tâche {title} avec {wordings} **')
    logger.info(f'** Terminée !')
