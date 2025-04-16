from celery import shared_task
from django.core.mail import send_mail
from django.utils.timezone import now, timedelta
from manager.models import Task



@shared_task
def send_task_reminder(task_id):
  try:
    task = Task.objects.get(id=task_id)
    if task.end_date > now():
      subject = f"Reminder: Task {task.title} is due now!"
      message = f"Hello\n\nThis is a reminder that your task '{task.title}' is due on {task.end_date}."
      send_mail(
        subject,
        message,
        'farukidris19@gmail.com',
        [task.author.email],
        fail_silently=False,
      )
      return f"Reminder sent for task {task.title}."
  except Task.DoesNotExist:
    return f"Task with id {task_id} does not exist."    

