from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
  first_name = models.CharField(max_length=50, blank=True, null=True)
  last_name = models.CharField(max_length=50, blank=True, null=True)
  username = models.CharField(max_length=50, unique=True)
  email = models.EmailField(max_length=100, unique=True)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  def __str__(self):
    return self.username

class Task(models.Model):
  PRIORITY = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High')
  )
  title = models.CharField(max_length=50)
  description = models.TextField()
  todo = models.CharField(max_length=50, blank=True, null=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task')
  priority = models.CharField(max_length=10, choices=PRIORITY, blank=True, default='low')
  start_date = models.DateTimeField(blank=True, null=True)
  end_date = models.DateTimeField(blank=True, null=True)
  completed = models.BooleanField(default=False)
  pending = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-updated_at']

  def __str__(self):
    return self.description[0:50]