from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from .models import Task

def landing(request):
    return redirect('login')


@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            due_date=due_date,
            priority=priority
        )
        return redirect('home')

    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "app/index.html", {'tasks': tasks})


#register
def register_views(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully. Please login.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, "app/register.html",{'form': form})

#Login
def login_views(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, "app/login.html", {'error': 'Invalid username or password'})

    return render(request, "app/login.html")

# Logout
def logout_views(request):
    logout(request)
    return redirect('login')


# Delete Task
@login_required(login_url='login')
def delete_task(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.delete()
    return redirect('home')

#update
@login_required(login_url='login')
def update_task(request, id):
    task = Task.objects.get(id=id, user=request.user)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.priority = request.POST.get('priority')
        task.save()
        return redirect('home')

    return render(request, 'app/update.html', {'task': task})

# Mark Task as Completed
@login_required(login_url='login')
def complete_task(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.completed = True
    task.save()
    return redirect('home')
