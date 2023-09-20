from django.shortcuts import render, redirect
from .models import Play, Record
from .forms import PlayForm, RecordForm


def plays(request):
    plays_list = Play.objects.order_by("year").reverse()
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
        return redirect("plays")

    context = {"play_id": play_id, "this_play": this_play}
    return render(request, "plays/play_site.html", context)


def records(request):
    records_list = Record.objects.order_by("id").reverse()
    return render(
        request,
        "plays/records.html",
        {"title": "Все записи", "records": records_list},
    )


def create_record(request):
    error = ""
    if request.method == "POST":
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("records")
        else:
            error = "Форма была неверной"
    form = RecordForm()
    context = {
        "form": form,
        "error": error,
    }

    return render(request, "plays/create_record.html", context)
