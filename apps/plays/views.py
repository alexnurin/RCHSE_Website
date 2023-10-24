from django.shortcuts import render, redirect
from .models import Play, Record
from .forms import PlayForm, RecordForm, FilterRecordsForm


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
    form = FilterRecordsForm()
    play_id = request.GET.get("play")

    if play_id:
        this_play = Play.objects.filter(id=play_id)[0]
        records_list = Record.objects.filter(play=this_play).order_by("id").reverse()
    else:
        records_list = Record.objects.order_by("id").reverse()

    if not form.is_valid():
        for f in form:
            print("ERROR: ", f.field, f.errors)

    return render(
        request,
        "plays/records.html",
        {
            "title": "Все записи",
            "records": records_list,
            "form": form,
        },
    )


def create_record(request):
    error = ""
    if request.method == "POST":
        form = RecordForm(data=request.POST, files=request.FILES)
        if form.is_valid() and form.check_duplicates():
            form.save()
            return redirect("records")
        else:
            errors_list = []
            for field, errors in form.errors.items():
                for error in errors:
                    errors_list.append(f"{field}: {error}")

            if not form.check_duplicates():
                errors_list.append(
                    "Нельзя дважды регистрироваться на одну и ту же постановку!"
                )

            context = {
                "form": form,
                "errors_list": errors_list,
            }
            print(errors_list)
            return render(request, "plays/create_record.html", context)

    play_id = request.GET.get("play")
    if not play_id:
        selectd_play = Play.objects.latest("id")
    else:
        selectd_play = Play.objects.filter(id=play_id)[0]

    first_name, last_name = None, None
    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
    print(f"user is non/authorised as {first_name} {last_name}")
    form = RecordForm(play=selectd_play, first_name=first_name, last_name=last_name)

    context = {
        "form": form,
        "error": error,
    }

    return render(request, "plays/create_record.html", context)
