from time import sleep
from django.core.mail import send_mail
from core.async_tasks.celery import app

# OperationalError
# [Errno 111] Connection refused
# from celery import shared_task
# @shared_task()

@app.task
def send_mail_task(from_email: str, subject: str, emails: list):
    print(f"on s'endort 5 secondes avant de lancer la tâche")
    sleep(5)
    print(f'démarrage de la tâche avec {from_email} {subject} {emails}')
    message = f'<p><strong>Message envoyé en différé !/strong></p>'
    print(f'{message}')
    # send_mail(subject=f'[Celery / Redis] {subject}',
    #           from_email=from_email,
    #           message='Message en différé',
    #           html_message=message,
    #           recipient_list=emails)
