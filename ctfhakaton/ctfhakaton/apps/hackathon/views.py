from django.views.generic import ListView
from .models import Hackathon

class FacultyView(ListView):
    """Вывод хакатонов"""
    model = Hackathon
    template_name = "hackathon/list_hackathon.html"
    context_object_name = 'hackathon'
