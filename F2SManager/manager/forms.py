from django import forms
from django.forms import ModelForm
from .models import User, Task
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class TaskForm(ModelForm):
  class Meta:
    model = Task
    fields = ['title', 'todo',  'description', 'priority', 'start_date', 'end_date']
    widgets = {
      'start_date': forms.DateInput(attrs={'type': 'date'}),
      'end_date': forms.DateInput(attrs={'type': 'date'}),
    }