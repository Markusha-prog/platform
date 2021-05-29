from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User  # Импорт стандартной модели пользователя Django
from django.contrib.auth.mixins import AccessMixin  # Модуль для проверки авторизован ли пользователь или нет
from .models import Profile, Team
from django.views.generic import View
from .forms import RegisterUserForm, LoginUserForm, CreateTeamForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'base.html')


class LoginRequiredMixin(AccessMixin):
    """ Проверка если пользователь не авторизован """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_page')
        return super().dispatch(request, *args, **kwargs)


class UnLoginRequiredMixin(AccessMixin):
    """ Проверка если пользователь авторизован """

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class RegisterUserView(UnLoginRequiredMixin, CreateView):
    """ Регистрация пользователя """
    model = User
    template_name = 'profile_user/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        my_password = form.cleaned_data['password1']
        email = form.cleaned_data['email']
        aut_user = authenticate(username=username, password=my_password, email=email)
        login(self.request, aut_user)
        return form_valid


class ProfileLoginView(UnLoginRequiredMixin, LoginView):
    """ Авторизация пользователя """
    template_name = 'profile_user/authorization.html'
    success_url = reverse_lazy('home')
    form_class = LoginUserForm

    def get_success_url(self):
        return self.success_url


class UserProfileView(DetailView, CreateView):
    """ Вывод профиля пользователя """
    model = Profile
    template_name = 'profile_user/profile.html'
    context_object_name = 'user_profile'
    form_class = CreateTeamForm
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        team_name = form.cleaned_data['team_name']
        cap = form.save(commit=False)
        cap.capitan = self.request.user
        form.save()
        team = Team.objects.get(team_name=team_name)
        team.user_teams.add(self.request.user)
        a = Team.objects.get(user_teams=self.request.user)
        user_team = Profile.objects.get(user=self.request.user)
        user_team.team_user = a
        if user_team.search_team == True:
            user_team.search_team = False
        user_team.save()
        return form_valid

    def get_success_url(self, **kwargs):
        if  kwargs != None:
            return reverse_lazy('profile', kwargs = {'pk': self.request.user.id})


class LogoutProfile(LoginRequiredMixin, LogoutView):
    """ Выход из аккаунта """
    next_page = reverse_lazy('home')

class CloseTeam(View, LoginRequiredMixin):
    """ Выход из команды """
    def get(self):
        a = Team.objects.get(user_teams=self.request.user)

