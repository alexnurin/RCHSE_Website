from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewUserForm

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('blog-home')
    else:
        form = NewUserForm()
    return render(request, 'users/register.html', {'form': form})