from django.shortcuts import render
from .models import Users


def index(request):
    users = Users.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'users': users})


def about(request):
    return render(request, 'main/about.html')
