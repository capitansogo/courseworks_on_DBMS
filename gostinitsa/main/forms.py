from django import forms
from django.forms import ModelForm, TextInput, FileInput, Select, DateInput

from .models import *


class BronForm(forms.ModelForm):
    class Meta:
        model = Bron
        fields = ['date_start', 'date_end']
        widgets = {
            'date_start': forms.DateInput(attrs={'type': 'date'}),
            'date_end': forms.DateInput(attrs={'type': 'date'}),
        }


class EditRoomForm(forms.ModelForm):
    class Meta:
        model = Nomer
        fields = ['name', 'cost', 'size', 'count_people', 'count_rooms', 'count_beds', 'photo', 'photo_mini']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'cost': TextInput(attrs={'class': 'form-control'}),
            'size': TextInput(attrs={'class': 'form-control'}),
            'count_people': TextInput(attrs={'class': 'form-control'}),
            'count_rooms': TextInput(attrs={'class': 'form-control'}),
            'count_beds': TextInput(attrs={'class': 'form-control'}),
            'photo': FileInput(attrs={'class': 'form-control'}),
            'photo_mini': FileInput(attrs={'class': 'form-control'}),
        }
