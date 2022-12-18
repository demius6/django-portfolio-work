from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm, UserRegisterForm, UserLoginForm, ContactForm


def home_page(request):
    tasks = Task.objects.order_by('-id')
    context = {'title': 'Yakimovich Aliaksandr',
               'tasks': tasks, }
    return render(request, 'mainpage/index.html', context)


def about(request):
    context = {'title': 'Yakimovich Aliaksandr'}
    return render(request, 'mainpage/about.html', context)



def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
               }
    return render(request, 'mainpage/create.html', context)

class TaskDetailView(DetailView):
    model = Task
    template_name = 'mainpage/task_page.html'
    context_object_name = 'task'
    form_class = TaskForm


class UpdateTask(UpdateView):
    model = Task
    template_name = 'mainpage/update_task.html'
    context_object_name = 'task'
    context = {'title': 'Yakimovich Aliaksandr'}
    form_class = TaskForm



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'mainpage/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
        return render(request, 'mainpage/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def test_mail(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'todojobs@mail.ru', ['yakimovich.99@mail.ru'], fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('mail')
            else:
                messages.error(request, 'Ошибка валидации')
    else:
        form = ContactForm()
    return render(request, 'mainpage/mail.html', {'form': form})
