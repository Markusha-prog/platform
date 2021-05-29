from django.urls import path
from .views import *


urlpatterns = [
    #Регистрация
    path('homepage/', home, name='home'),
    ]