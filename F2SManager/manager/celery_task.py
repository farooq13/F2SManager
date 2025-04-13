from celery import shared_task
from django.core.mail import send_mail
from .models import Task
from django.utils import timezone
from datetime import timedelta


@shared_task
def send_deadline_reminders():
  tomorrow = timezone.now().date() + timedelta(days=1)
  tasks = Task.objects.filter(end_date=tomorrow, completed=False)

  for task in tasks:
    send_mail(
      subject=f"Reminder: Task '{task.title}' is due tomorror",
      message=f'The deadline for your task "{task.title}" is tomorrow. Please make sure to complete it.',
      from_email="farukidris19@gmail.com",
      reciepient_list=[task.author.email]
    )