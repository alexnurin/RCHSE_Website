from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewUserForm
from .models import User

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('users')
    else:
        form = NewUserForm()
    return render(request, 'users/register.html', {'form': form})


def users(request):
    users = User.objects.order_by('-id')
    return render(request, 'users/users.html', {'title': 'Пользователи', 'users': users})

def profile(request):
    return render(request, 'users/profile.html', {'title': 'Пользователь'})