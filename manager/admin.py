from django.contrib import admin
from .models import User, Task
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
  list_display = ('username', 'first_name', 'last_name')


class TaskAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'todo', 'priority', 'completed', 'start_date', 'end_date', 'created_at', 'updated_at')
 

admin.site.register(User, UserAdmin)
admin .site.register(Task, TaskAdmin)