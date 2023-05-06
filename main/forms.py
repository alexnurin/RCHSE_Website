from .models import Users
from django.forms import ModelForm, TextInput, Textarea


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'description']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание',
            }),
        }
