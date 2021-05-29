from django.urls import path
from .views import *

urlpatterns = [
    # Регистрация
    path('list_hackathons/', FacultyView.as_view(), name='list_hackathons'),

]
