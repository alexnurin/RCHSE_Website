from django.shortcuts import render, redirect
from .models import Users, Games
from .forms import UsersForm, GamesForm


def index(request):
    return render(request, 'main/main.html', {'title': 'Главная страница сайта'})


def users(request):
    users = Users.objects.order_by('-id')
    return render(request, 'main/users.html', {'title': 'Пользователи', 'users': users})


def games(request):
    games_list = Games.objects.order_by('id')
    return render(request, 'main/games.html', {'title': 'Все игры', 'games': games_list})


def about(request):
    return render(request, 'main/about.html')


def create_game(request):
    error = ''
    if request.method == 'POST':
        form = GamesForm(request.POST, request.FILES)
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


def game(request):
    game_id = request.GET.get('id')

    this_game = Games.objects.filter(id=game_id)
    if this_game:
        this_game = this_game[0]
    else:
        this_game = "empty"

    context = {
        'game_id': game_id,
        'this_game': this_game
    }
    return render(request, 'main/game_site.html', context)