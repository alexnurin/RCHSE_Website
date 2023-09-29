from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewUserForm, LoginUserForm
from .models import User
import django.contrib.auth as dj_auth


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = dj_auth.authenticate(username=username, password=password)
            dj_auth.login(request, user)
            return redirect("home")
    else:
        form = NewUserForm()
    return render(request, "users/register.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = LoginUserForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = dj_auth.authenticate(username=username, password=password)
            if user:
                dj_auth.login(request, user)
                return redirect("home")
    else:
        form = LoginUserForm()
    return render(request, "users/login.html", {"form": form})


def users(request):
    users = User.objects.order_by("-last_login")
    return render(
        request, "users/users.html", {"title": "Пользователи", "users": users}
    )


def profile(request):
    context = {
        "title": "Пользователь",
    }
    return render(request, "users/profile.html", context)


def user_logout(request):
    dj_auth.logout(request)
    return redirect("home")


def login_via_vk(request):
    if request.user.is_authenticated:
        dj_auth.logout(request)
    return redirect("login/vk-oauth2")
