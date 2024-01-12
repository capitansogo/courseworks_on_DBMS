from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .models import *
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, EmailInput, NumberInput, Select, FileInput, \
    SplitDateTimeWidget, NullBooleanSelect
from django import forms


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username', 'password1', 'password2', 'first_name', 'last_name', 'patronymic', 'phone', 'email',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилию'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите отчество'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите дату рождения'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}),
        }


class AddToCartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите количество'}),
        }


class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'


class AddMaterialForm(ModelForm):
    class Meta:
        model = Materials
        fields = ['name', 'type', 'manufacturer', 'unit_of_measurement', 'price', 'description', 'price_delivery',
                  'photo', 'photo2', 'in_stock']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            'type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Введите тип'}),
            'manufacturer': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Введите производителя'}),
            'unit_of_measurement': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Введите единицу измерения'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите цену'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
            'price_delivery': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Введите цену доставки'}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Введите фото'}),
            'photo2': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Введите фото'}),
            'in_stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите наличие'}),
        }
