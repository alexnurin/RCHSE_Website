from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.http import HttpResponse

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def index(request):
    return render(request, "main/main.html", {"title": "Главная страница сайта"})


def about(request):
    return render(request, "main/about.html")
