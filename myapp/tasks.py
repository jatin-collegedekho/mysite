from celery import shared_task

@shared_task
def demo_celery_task():
    for _ in range(10):
        print("Celery Task Executed !!!")

