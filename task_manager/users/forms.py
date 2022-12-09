from .models import User
from django.forms import ModelForm, TextInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'nickname']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя',
                'maxlength': '150'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию',
                'maxlength': '150'
            }),
            'nickname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя пользователя',
                'maxlength': '150'
            }),
        }
