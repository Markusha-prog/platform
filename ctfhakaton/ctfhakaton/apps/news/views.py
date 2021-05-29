from django.shortcuts import render
from django.views.generic import DetailView
from .models import News

class NewsView(DetailView):
    """ Вывод профиля пользователя """
    model = News
    template_name = 'news/detail_news.html'
    context_object_name = 'news_detail'
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)