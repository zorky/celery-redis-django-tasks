from time import sleep
from celery import shared_task
from django.core.mail import send_mail

import logging
logger = logging.getLogger('django')

@shared_task()
def send_mail_task(from_email: str, subject: str, emails: list):
    sleep(5)
    logger.info(f'démarrage de la tâche avec {from_email} {subject} {emails}')
    message = f'<p><strong>Message envoyé en différé !/strong></p>'
    send_mail(subject=f'[Celery / Redis] {subject}',
              from_email=from_email,
              message='Message en différé',
              html_message=message,
              recipient_list=emails)
