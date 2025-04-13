from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('task_detail/<str:pk>/', views.task_detail, name='task-detail'),
  path('login/', views.login_user, name='login'),
  path('logout/', views.login_user, name='logout'),
  path('register/', views.register_user, name='register'),

  path('create/', views.create_task, name='create-task'),
  path('update/<int:pk>/', views.update_task, name='update-task'),
  path('delete/<int:pk>/', views.delete_task, name='delete-task'),

]