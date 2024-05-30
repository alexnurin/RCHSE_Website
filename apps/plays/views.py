from django.shortcuts import render, redirect, get_object_or_404
from .models import Play, Record
from .forms import PlayForm, RecordForm, FilterRecordsForm


def plays(request):
    plays_list = Play.objects.order_by("play_id").reverse()
    return render(
        request, "plays/plays.html", {"title": "Все постановки", "plays": plays_list}
    )


def create_play(request):
    if request.method == "POST":
        form = PlayForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("plays")
        error = "Форма была неверной"
    else:
        form = PlayForm()
        error = ""
    context = {
        "form": form,
        "error": error,
    }
    return render(request, "plays/create_play.html", context)


def play(request):
    play_id = request.GET.get("play_id")
    this_play = get_object_or_404(Play, play_id=play_id)
    context = {"play_id": play_id, "this_play": this_play}
    return render(request, "plays/play_site.html", context)


def records(request):
    form = FilterRecordsForm(request.GET or None)
    records_list = Record.objects.order_by("-record_id")

    if form.is_valid():
        play = form.cleaned_data.get('play')
        if play:
            records_list = records_list.filter(play=play)
    return render(request, "plays/records.html", {"title": "Все записи", "records": records_list, "form": form})


def create_record(request):
    if request.method == "POST":
        form = RecordForm(data=request.POST, files=request.FILES)
        if form.is_valid() and form.check_duplicates():
            form.save()
            return redirect("records")
        errors_list = form.errors.get_json_data(escape_html=True)
        if not form.check_duplicates():
            errors_list.append(
                {"field": "__all__", "message": "Нельзя дважды регистрироваться на одну и ту же постановку!"})
    else:
        if Play.objects.exists():
            play_id = request.GET.get("play_id")
            selected_play = get_object_or_404(Play, play_id=play_id) if play_id else Play.objects.latest("date")
        else:
            selected_play = None

        if request.user.is_authenticated:
            form = RecordForm(play=selected_play, first_name=request.user.first_name, last_name=request.user.last_name)
        else:
            form = RecordForm(play=selected_play)
        errors_list = []

    context = {"form": form, "errors_list": errors_list}
    return render(request, "plays/create_record.html", context)
