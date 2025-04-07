from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import User, Task
from django.http import HttpResponse
from .forms import RegistrationForm, TaskForm


def login_user(request):
  page = 'login'

  if request.user.is_authenticated:
    return redirect('home')
  
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
      user = User.objects.get(email=email)
    except:
      messages.error(request, 'Email does not exist')

    user = authenticate(request, email=email, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.error(request, 'Email or Password does not exist')

  context = {'page': page}
  return render(request, 'manager/register_login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def register_user(request):
  form = RegistrationForm()

  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.username = user.username.lower()
      user.save()
      login(request, user)
      return redirect('home')
    else:
      messages.error(request, 'An error occured')
  context = {'form': form}
  return render(request, 'manager/register_login.html', context)


def home(request):
  query = request.GET.get('query') if request.GET.get('query') != None else ''
  priority = request.GET.get('priority') if request.GET.get('priority') != None else ''
  status = request.GEt.get('status') if request.GET.get('status') != None else ''
  sort = request.GET.get('sort') if request.GET.get('sort') != None else ''

  tasks = Task.objects.all()

  if priority:
    tasks = tasks.filter(priority=priority)
  else:
    tasks = Task.objects.filter(
      Q(title__icontains=query)|
      Q(description__icontains=query)|
      Q(todo__icontains=query)
    )

  if sort == 'created_asc':
    tasks = tasks.order_by('created_at')
  elif sort == 'created_desc':
    tasks = tasks.order_by('-created_at')
  elif sort == 'start_asc':
    tasks.order_by('start_date')
  elif sort == 'start_desc':
    tasks.order_by('-start_date')
  elif sort == 'end_asc':
    tasks.order_by('end_date')
  elif sort == 'end_desc':
    tasks.order_by('-end_date')

  if status == 'completed':
    tasks.filter(completed=True)
  elif status == 'pending':
    tasks.filter(pending=True)
    
  context = {
    'tasks': tasks,
    'priority': priority,
    'query': query,
  }
  return render(request, 'manager/home.html', context)


@login_required(login_url='loging')
def task_detail(request, pk):
  task = get_object_or_404(Task, pk=pk)
  context = {
    'task': task
  }
  return render(request, 'manager/task_detail.html', context)


@login_required(login_url='login')
def create_task(request):
  form = TaskForm()
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      new_task = form.save(commit=False)
      new_task.author = request.user
      new_task.save()
      return redirect('home')
    else:
      messages.error(request, 'Something is wrong')

  context = {'form': form}
  return render(request, 'manager/create_task.html', context)


@login_required(login_url='login')
def update_task(request, pk):
  context = {}
  return render(request, 'manager/update_task.html', context)

@login_required(login_url='login')
def delete_task(request, pk):
  return render(request, 'manager/delete_task.html')



def task_edit(request, pk):
  task_to_edit = get_object_or_404(Task, pk=pk)
  form = TaskForm(instance=task_to_edit)

  if request.method == 'POST':
    task_to_edit.author = request.user
    task_to_edit.title = request.POST.get('title')
    task_to_edit.priority = request.POST.get('priority')
    task_to_edit.task = request.POST.get('task')

  context = {
    'task_to_edit': task_to_edit,
    'form': form
  }
  return render(request, 'manager/update_task.html', context)


@login_required(login_url='login')
def delete_task(request, pk):
  task = get_object_or_404(Task, pk=pk)

  if request.user != task.author:
    return HttpResponse('You are not allowed to delete this task')

  if request.method == 'POST':
    task.delete()
    messages.info(request, 'Task was deleted successfully')
    return redirect('home')
  
  context = {'task': task}
  return render(request, 'manager/delete_task.html', context)


