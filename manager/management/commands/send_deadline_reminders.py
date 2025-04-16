from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils.timezone import now, timedelta
from manager.models import Task


class Command(BaseCommand):
  help = 'Send email reminders for tasks due tomorrow'

  def handle(self, *args, **kwargs):
    tomorrow = now().date() + timedelta(days=1)
    tasks = Task.objects.filter(end_date=tomorrow, completed=False)

    for task in tasks:
      reciepient_email = task.user.email
      send_mail(
        subject=f"Reminder: Task '{task.title}' is due tomorrow",
        message=f"Your task \"{task.title}\" is due on {task.end_date}. Don't forget to complete it!",
        from_email='farukidris19@gmail.com',
        reciepient_list=[reciepient_email],
        fail_silently=False,
      )

    self.stdout.write(self.style.SUCCESS('Successfully sent email reminders for tasks due tomorrow.'))