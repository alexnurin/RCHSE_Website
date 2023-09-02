from .models import Games
from django.forms import ModelForm, TextInput, Textarea


class GamesForm(ModelForm):
    class Meta:
        model = Games
        fields = ['title', 'description', 'image']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание',
            }),
        }
