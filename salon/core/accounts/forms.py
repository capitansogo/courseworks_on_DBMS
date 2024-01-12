from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import *


class MyDateInput(forms.DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'


class UserCreateForm(UserCreationForm):
    class Meta:
        model = Users
        fields = (
            'username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}),
        }

        def __init__(self, *args, **kwargs):
            super(UserCreateForm, self).__init__(*args, **kwargs)
            self.fields.help_text = None


class BuyMaterialsForm(ModelForm):
    class Meta:
        model = Purchases
        fields = '__all__'
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Выберите пользователя'}),
            'material': forms.Select(attrs={'class': 'form-control', 'visibility': 'hidden'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'гггг-мм-дд'}),
        }


class EditMaterialsForm(ModelForm):
    class Meta:
        model = Materials
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите цену'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
            'cost': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Введите описание', 'disabled': True}),
        }


class Write_offsForm(ModelForm):
    class Meta:
        model = Write_offs
        fields = '__all__'
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Выберите пользователя'}),
            'material': forms.Select(attrs={'class': 'form-control', 'visibility': 'hidden'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'гггг-мм-дд'}),
        }


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
        widgets = {
            'client': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Выберите пользователя', 'disabled': True}),
            'types_of_services': forms.Select(attrs={'class': 'form-control', 'visibility': 'hidden'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'гггг-мм-дд'}),
        }
