from .models import Game
from django.forms import ModelForm, TextInput, Textarea


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ["title", "description", "image"]
        widgets = {
            "title": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название",
                }
            ),
            "description": Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите описание",
                }
            ),
        }
