from .models import Play, Record

from django.forms import (
    Form,
    ModelForm,
    TextInput,
    RadioSelect,
    Textarea,
    ModelChoiceField,
    Select,
)


class PlayForm(ModelForm):
    class Meta:
        model = Play
        fields = ["game", "date"]


class FilterRecordsForm(Form):
    play = ModelChoiceField(
        label="Постановка",
        queryset=Play.objects.all().order_by("date").reverse(),
        required=False,
        empty_label="Все постановки",
    )


class RecordForm(ModelForm):
    def __init__(self, play=None, first_name=None, last_name=None, *args, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)
        print(play, first_name, last_name)
        if play:
            self.fields["play"].initial = play
        if first_name:
            self.fields["name"].initial = first_name
        if last_name:
            self.fields["surname"].initial = last_name

    def check_duplicates(self):
        duplicates = Record.objects.filter(
            name=self.cleaned_data["name"],
            surname=self.cleaned_data["surname"],
            play=self.cleaned_data["play"],
        )
        return not duplicates

    class Meta:
        model = Record
        fields = [
            "play",
            "name",
            "surname",
            "need_pass",
            "patronymic",
            "vk_link",
            "preferable_mates",
            "preferable_role",
            "first_game",
        ]
        labels = {
            "play": "Постановка:",
        }
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
