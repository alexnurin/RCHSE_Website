from django.shortcuts import render, redirect
from .models import Play
from .forms import PlayForm


def plays(request):
    plays_list = Play.objects.order_by("id")
    return render(
        request, "plays/plays.html", {"title": "Все постановки", "plays": plays_list}
    )


def create_play(request):
    error = ""
    if request.method == "POST":
        form = PlayForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("plays")
        else:
            error = "Форма была неверной"
    form = PlayForm()
    context = {
        "form": form,
        "error": error,
    }

    return render(request, "plays/create_play.html", context)


def play(request):
    play_id = request.GET.get("id")

    this_play = Play.objects.filter(id=play_id)
    if this_play:
        this_play = this_play[0]
    else:
        this_play = "empty"

    context = {"play_id": play_id, "this_play": this_play}
    return render(request, "plays/play_site.html", context)
