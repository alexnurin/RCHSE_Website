from django.shortcuts import render, redirect
from .models import Game
from .forms import GameForm
from apps.plays.models import Play


def games(request):
    all_games = Game.objects.order_by("game_id")
    plays_list = {}
    for game in all_games:
        plays_list[game] = Play.objects.filter(game=game).order_by("date").reverse()[:5]
    return render(
        request,
        "games/games.html",
        {
            "title": "Все игры",
            "games": all_games,
            "plays_list": plays_list,
        },
    )


def create_game(request):
    error = ""
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("games")
        else:
            error = form.errors
            print(form.errors)

    form = GameForm()
    context = {
        "form": form,
        "error": error,
    }

    return render(request, "games/create_game.html", context)


def delete_game(request):
    game_id = request.GET.get("game_id")
    game = Game.objects.filter(id=game_id)
    if game:
        game[0].delete()
    return redirect("games")


def game(request):
    game_id = request.GET.get("game_id")

    this_game = Game.objects.filter(game_id=game_id)
    if this_game:
        this_game = this_game[0]
    else:
        return redirect("games")

    plays = Play.objects.filter(game=this_game).order_by("date").reverse()[:5]

    context = {
        "game_id": game_id,
        "this_game": this_game,
        "plays": plays,
    }
    return render(request, "games/game_site.html", context)
