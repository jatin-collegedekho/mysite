import os
from celery import Celery

# setting the Django settings module.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "mysite.settings")

app = Celery('log')
app.config_from_object('django.conf:settings', namespace="CELERY")

# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks()
