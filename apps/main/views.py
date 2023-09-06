from django.shortcuts import render

def index(request):
    return render(request, 'main/main.html', {'title': 'Главная страница сайта'})

def about(request):
    return render(request, 'main/about.html')

