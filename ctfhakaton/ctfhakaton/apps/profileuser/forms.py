from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _


class RegisterUserForm(UserCreationForm, forms.ModelForm):
    """ Форма регистрации пользователя """
    error_messages = {
        'password_mismatch': _("Пароли различаются"),
    }

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs.update({'placeholder': 'Логин*', 'class': 'form-control'})
            self.fields['username'].widget.attrs['maxlength'] = "20"
            self.fields['username'].help_text = ''
            self.fields['email'].widget = forms.DateInput(attrs={'type': "email"})
            self.fields['email'].widget.attrs.update({'placeholder': 'Почта*', 'class': 'form-control'})
            self.fields['password1'].widget.attrs.update(
                {'placeholder': 'Пароль*', 'class': 'form-control', "id": "password-input", "name": "password"})
            self.fields['password2'].widget.attrs.update({'placeholder': 'Повторите пароль*', 'class': 'form-control'})
            self.fields['password1'].help_text = None
            self.fields['password2'].help_text = ''


class LoginUserForm(AuthenticationForm, forms.ModelForm):
    """ Форма авторизации пользователя """
    error_messages = {
        'invalid_login': _(
            "Неверное имя аккаунта или пароль."
        ),
    }
    class Meta:
        model = User
        fields = ('username', 'password')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs.update({'placeholder' : 'Введите логин', 'class' : 'form-control'})
            self.fields['password'].widget.attrs.update({'placeholder' : 'Введите пароль', 'class' : 'form-control', "id" : "password-input", "name" : "password" })
