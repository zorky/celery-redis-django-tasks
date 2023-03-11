""" Celery config """
broker_url = "redis://redis:6379/0"

result_backend = "redis://redis:6379/1"
result_expires = 600  # 10 min

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
