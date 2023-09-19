from django.forms import EmailField, TextInput
from django.contrib.auth.forms import UserCreationForm
from .models import User


class NewUserForm(UserCreationForm):
    email = EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        widgets = {
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
            "email": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите почту",
                }
            ),
        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
