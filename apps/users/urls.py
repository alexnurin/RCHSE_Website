from django.urls import path
from . import views

urlpatterns = [
    path("users", views.users, name="users"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("login_via_vk", views.login_via_vk, name="login_via_vk"),
    path("logout", views.user_logout, name="logout"),
    path("profile", views.profile, name="profile"),
    path("assign_moderator/<int:user_id>/", views.assign_moderator, name='assign_moderator'),
]
