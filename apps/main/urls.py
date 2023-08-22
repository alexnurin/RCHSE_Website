from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('users', views.users, name='users'),
    path('about', views.about, name='about'),
    path('games', views.games, name='games'),
    path('game', views.game, name='game'),
    path('create_game', views.create_game, name='create'),
]
