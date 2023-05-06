from django.shortcuts import render, redirect
from .models import Users
from .forms import UsersForm


def index(request):
    users = Users.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'users': users})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = UsersForm()
    context = {
        'form': form,
        'error': error,
    }

    return render(request, 'main/create.html', context)
