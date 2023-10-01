from django.shortcuts import render, redirect
from .models import Game
from .forms import GameForm


def games(request):
    games_list = Game.objects.order_by("id")
    return render(
        request, "games/games.html", {"title": "Все игры", "games": games_list}
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


def game(request):
    game_id = request.GET.get("id")

    this_game = Game.objects.filter(id=game_id)
    if this_game:
        this_game = this_game[0]
    else:
        return redirect("games")

    context = {"game_id": game_id, "this_game": this_game}
    return render(request, "games/game_site.html", context)
