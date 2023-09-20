from .models import Play
from django.forms import ModelForm, NumberInput, CharField


class PlayForm(ModelForm):
    class Meta:
        model = Play
        fields = ["year", "game"]
        widgets = {
            "year": NumberInput(attrs={"class": "form-control"}),
        }
