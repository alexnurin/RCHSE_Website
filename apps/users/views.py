from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .forms import NewUserForm, UserProfileForm
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth import login as auth_login, authenticate
from django.views import View
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as dj_auth_login, logout as dj_auth_logout


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect("home")
    else:
        form = NewUserForm()
    return render(request, "users/register.html", {"form": form})


class CustomLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                dj_auth_login(request, user)
                if Group.objects.get(name='Admin') in user.groups.all():
                    return redirect(reverse('two_factor:setup'))
                else:
                    return redirect('home')
        return render(request, 'users/login.html', {'form': form})


def all_users(request):
    all_users_list = User.objects.order_by("-last_login")
    return render(request, "users/users.html", {"title": "Пользователи", "users": all_users_list})


def profile(request):
    user = request.user
    form = UserProfileForm(instance=user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()

    context = {
        "title": "Пользователь", 'user': user, 'form': form
    }
    return render(request, "users/profile.html", context)


def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'edit_profile.html', {'form': form})


def user_logout(request):
    dj_auth_logout(request)
    return redirect("home")


def login_via_vk(request):
    if request.user.is_authenticated:
        dj_auth_logout(request)
    return redirect("login/vk-oauth2")


@user_passes_test(lambda u: u.is_staff)  # Только администраторы могут назначать модераторов
def assign_moderator(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_admin = True
    user.save()
    moderator_group = Group.objects.get(name='Moderators')
    user.groups.add(moderator_group)
    return redirect('users')
# Замените 'home' на имя вашего маршрута главной страницы
