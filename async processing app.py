from celery import Celery

celery = Celery('tasks', broker='pyamqp://guest@localhost//')

@celery.task
def process_transaction(data):
    # simulate fraud detection logic
    if data['amount'] > 100000:
        return "Flagged for review"
    return "Approved"