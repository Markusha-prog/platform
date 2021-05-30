from django.urls import path
from .views import *

urlpatterns = [
    # Регистрация
    path('list_hackathons/', FacultyView.as_view(), name='list_hackathons'),
    path('qr_generate/', QrGenerate.as_view(), name='qr_generate'),
    path('start_generate_qr/', start_generate_qr, name='start_generate_qr'),
    path('evaluation/', Evaluation.as_view(), name='evaluation'),
    path('info_team/', info_team, name='info_team'),
]
