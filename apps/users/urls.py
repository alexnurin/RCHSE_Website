from django.urls import path
from . import views

urlpatterns = [
    path("users", views.users, name="users"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.user_logout, name="logout"),
    path("profile", views.profile, name="profile"),
]
