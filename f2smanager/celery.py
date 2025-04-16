import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'f2smanager.settings')

app = Celery('f2smanager')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()