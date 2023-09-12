from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from myapp.tasks import demo_celery_task


@receiver(pre_save, sender=User)
def demo_pre_save_signal(*args, **kwargs):
    print("In Pre Save !!!")
    demo_celery_task.delay()