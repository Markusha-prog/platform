from django.urls import path
from .views import *

urlpatterns = [
    path('news_detail/=<int:pk>', NewsView.as_view(), name='news_detail'),
]