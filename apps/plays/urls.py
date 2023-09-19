from django.urls import path
from . import views

urlpatterns = [
    path("plays", views.plays, name="plays"),
    path("play", views.play, name="play"),
]
