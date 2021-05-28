from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.models import User     #Импорт стандартной модели пользователя Django
from django.contrib.auth.mixins import AccessMixin #Модуль для проверки авторизован ли пользователь или нет
from .models import Profile
from .forms import RegisterUserForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login

class UnLoginRequiredMixin(AccessMixin):
    """ Проверка если пользователь авторизован """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

class RegisterUserView(UnLoginRequiredMixin, CreateView):
    """ Регистрация пользователя """
    model = User
    template_name = 'profileuser/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('send_verefication')
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        my_password = form.cleaned_data['password1']
        email = form.cleaned_data['email']
        aut_user = authenticate(username = username, password = my_password, email = email)
        login(self.request, aut_user)
        return form_valid
