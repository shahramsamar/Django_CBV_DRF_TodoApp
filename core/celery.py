import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')



# from accounts.tasks import send_email
# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls send email() every 10 seconds.
#     sender.add_periodic_task(10.0, send_email.s(), name=' send email every 10 seconds')

from celery.schedules import crontab

# تنظیمات Beat
app.conf.beat_schedule = {
    'delete-done-posts-every-10-minutes': {
        'task': 'accounts.tasks.delete_done_post',
        'schedule': crontab(minute='*/10'),
    },
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')