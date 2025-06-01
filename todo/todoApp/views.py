from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from django.core.paginator import Paginator
from .services import detect_priority



# Create your views here.
@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user).order_by('-id')
    paginator = Paginator(todos, 5)  # Show 5 todos per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})

@login_required
def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = detect_priority(title)
        Todo.objects.create(user=request.user, title=title, description=description, priority=priority)
        return redirect('todo_list')

@login_required
def complete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

@login_required
def delete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.delete()
    return redirect('todo_list')

@login_required
def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        priority = detect_priority(todo.title)

        todo.title = todo.title
        todo.description = todo.description
        todo.priority = priority
        todo.save()
        return redirect('todo_list')
      

    return render(request, 'update.html', {'todo': todo})


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('todo_list')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')