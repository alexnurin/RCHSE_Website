from django.shortcuts import render, redirect
from .models import Users, Games
from .forms import UsersForm, GamesForm


def index(request):
    users = Users.objects.order_by('-id')
    return render(request, 'main/main.html', {'title': 'Главная страница сайта', 'users': users})


def games(request):
    games_list = Games.objects.order_by('-id')
    return render(request, 'main/games.html', {'title': 'Все игры', 'games': games_list})


def about(request):
    return render(request, 'main/about.html')


def create_game(request):
    error = ''
    if request.method == 'POST':
        form = GamesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = GamesForm()
    context = {
        'form': form,
        'error': error,
    }

    return render(request, 'main/create_game.html', context)


def game_site(request):
    result = ''
    for el in request.GET.iteritems:
        result += el + '\n'

    return render(request, )
