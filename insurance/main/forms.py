from django import forms

from .models import *


# форма автостраховки
class AutoInsuranceForm(forms.ModelForm):
    class Meta:
        model = AutoInshurance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].widget.attrs.update({'class': 'form-select'})
        self.fields['date'].widget = forms.DateInput(attrs={'class': 'form-control'})
        self.fields['client'].queryset = User.objects.filter(role__name='Клиент')
        self.fields['number'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['mark'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['model'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['vin'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['year'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['engine'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['power'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['color'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['price'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['agent'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['salary'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['percent_agent'].widget = forms.TextInput(attrs={'class': 'form-control'})


# форма медицинской страховки
class HealthInsuranceForm(forms.ModelForm):
    class Meta:
        model = HealthInshurance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].widget.attrs.update({'class': 'form-select'})
        self.fields['date'].widget = forms.DateInput(attrs={'class': 'form-control'})
        self.fields['client'].queryset = User.objects.filter(role__name='Клиент')
        self.fields['agent'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['salary'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['percent_agent'].widget = forms.TextInput(attrs={'class': 'form-control'})


# форма имущественной страховки
class PropertyInsuranceForm(forms.ModelForm):
    class Meta:
        model = PropertyInshurance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].widget.attrs.update({'class': 'form-select'})
        self.fields['date'].widget = forms.DateInput(attrs={'class': 'form-control'})
        self.fields['client'].queryset = User.objects.filter(role__name='Клиент')
        self.fields['city'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['street'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['house'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['flat'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['type_building'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['agent'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['salary'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['percent_agent'].widget = forms.TextInput(attrs={'class': 'form-control'})


# форма добавления пользователя
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'role', 'first_name', 'last_name', 'email', 'phone', 'adress', 'passport']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].widget.attrs.update({'class': 'form-select'})
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['password'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['role'].queryset = Roles.objects.filter(name='Клиент')
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control'})
        self.fields['phone'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['adress'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['passport'].widget = forms.TextInput(attrs={'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


# форма ввода дат для отчета по зарплате
class SalaryReportForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    start_date.label = 'Начальная дата'
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date.label = 'Конечная дата'
