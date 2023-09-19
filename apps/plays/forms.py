from .models import Play
from django.forms import ModelForm, IntegerField


class PlayForm(ModelForm):
    class Meta:
        model = Play
        fields = ["year"]
        widgets = {
            "year": IntegerField(),
        }
