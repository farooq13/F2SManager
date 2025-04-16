from django.core.mail import send_mail
from django.utils.timezone import now, timedelta
from .models import Task


def send_task_reminders():
  tomorrow = now().date() + timedelta(days=1)
  tasks = Task.objects.filter(end_date=tomorrow, is_completed=False)

  for task in tasks:
    send_mail(
      subject=f"Reminder: Task '{task.title}' is due tomorrow",
      message=f"Your task\"{task.title}\" is due on {task.end_date}. Don't forget to complete it!",
      from_mail='farukidris19@gmail.com',
      recipient_list=['task.user.email'],
      fail_silently=False,
    )