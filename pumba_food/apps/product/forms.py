from django import forms
from .models import ContactUs

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ваш email', 'required': True}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ваш телефон', 'required': True}),
            'message': forms.Textarea(attrs={'placeholder': 'Ваше сообщение', 'required': True}),
        }
        error_messages = {
            'name': {
                'required': 'Это поле обязательно для заполнения.',
                'invalid': 'Введите корректное имя.',
            },
            'email': {
                'required': 'Это поле обязательно для заполнения.',
                'invalid': 'Введите корректный email.',
            },
            'phone': {
                'required': 'Это поле обязательно для заполнения.',
                'invalid': 'Введите корректный телефон.',
            },
            'message': {
                'required': 'Это поле обязательно для заполнения.',
                'min_length': 'Сообщение слишком короткое.',
            },
        }