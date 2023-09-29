from django.forms import EmailField, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )
        widgets = {
            "username": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите никнейм",
                }
            ),
            "first_name": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите имя",
                }
            ),
            "last_name": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите фамилию",
                }
            ),
        }

    # def save(self, commit=True):
    #     user = super(NewUserForm, self).save(commit=False)
    #     user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
