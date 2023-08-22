from .models import Users, Games
from django.forms import ModelForm, TextInput, Textarea


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'email']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя',
            }),
            'email': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту',
            }),
        }


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
