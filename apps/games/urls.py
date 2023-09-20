from django.urls import path
from . import views

urlpatterns = [
    path("games", views.games, name="games"),
    path("game", views.game, name="game"),
    path("create_game", views.create_game, name="create_game"),
]
