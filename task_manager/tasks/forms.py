from django import forms
from django.forms import TextInput, Textarea, Select

from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название задачи',
                'maxlength': '100'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание задачи',
                'maxlength': '100'
            }),
            'status': Select(attrs={
                'class': 'form-control'
            }),
            'executor': Select(attrs={
                'class': 'form-control'
            }),
            'labels': Select(attrs={
                'class': 'form-control'
            })
        }
