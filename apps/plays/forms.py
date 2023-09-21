from .models import Play, Record

from django.forms import (
    ModelForm,
    NumberInput,
    TextInput,
    RadioSelect,
    Textarea,
)


class PlayForm(ModelForm):
    class Meta:
        model = Play
        fields = ["year", "game"]
        widgets = {
            "year": NumberInput(attrs={"class": "form-control"}),
        }


class RecordForm(ModelForm):
    def __init__(self, play=None, *args, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)
        if play:
            self.fields["play"].initial = play

    class Meta:
        model = Record
        fields = [
            "name",
            "surname",
            "need_pass",
            "patronymic",
            "vk_link",
            "preferable_mates",
            "preferable_role",
            "first_game",
            "play",
        ]
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите имя",
                }
            ),
            "surname": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите фамилию",
                }
            ),
            "need_pass": RadioSelect(choices=[("YES", "Да"), ("NO", "Нет")]),
            "patronymic": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите отчество",
                }
            ),
            "vk_link": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите ВК",
                }
            ),
            "preferable_mates": Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Мастера и/или соигроки",
                }
            ),
            "preferable_role": Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "От более к менее предпочтительному",
                }
            ),
            "first_game": RadioSelect(choices=[("YES", "Да"), ("NO", "Нет")]),
        }
