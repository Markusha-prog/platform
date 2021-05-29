from django.urls import path
from .views import *

urlpatterns = [
    # Регистрация
    path('reg-user/', RegisterUserView.as_view(), name='register_page'),
    path('auth-user/', ProfileLoginView.as_view(), name='auth_page'),
    path('profile=<int:pk>', UserProfileView.as_view(), name='profile'), #Профиль пользователя
    path('logout', LogoutProfile.as_view(), name='logout_page'),
    path('', home, name='home'),
    path('close_team/', CloseTeam.as_view(), name='close_team')
]
