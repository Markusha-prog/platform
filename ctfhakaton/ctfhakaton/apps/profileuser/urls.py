from django.urls import path
from .views import RegisterUserView

urlpatterns = [
    #Регистрация
    path('registration/', RegisterUserView.as_view(), name='register_page'),
    ]