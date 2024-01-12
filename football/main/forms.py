from django import forms
from .models import Matches


class MatchForm(forms.ModelForm):
    class Meta:
        model = Matches
        fields = '__all__'
