from django.views.generic import ListView, View
from .models import Hackathon, File_QR
from django.shortcuts import render
from django.http import JsonResponse
from .functions.generate_qr import generate_qr
from django.http import FileResponse
from profile_user.models import Team


class FacultyView(ListView):
    """Вывод хакатонов"""
    model = Hackathon
    template_name = "hackathon/list_hackathon.html"
    context_object_name = 'hackathon'


class QrGenerate(View):
    """ Функция генерации QR-тегов """
    def get(self, request):
        context = {
        }
        template = "hackathon/qr_generate.html"  # Шаблон
        return render(request, template, context)


def start_generate_qr(request):
    field = request.GET.get('inputValue')
    flag = generate_qr(field)
    if flag == False:
        answer = False
    else:
        answer = File_QR.objects.get(pk=flag)
        answer = answer.file.url
    data = {
        'response': answer,
    }
    return JsonResponse(data)

class Evaluation(View):
    def get(self, request):
        teams = Team.objects.all()
        context = {
            'teams': teams,
        }
        template = "hackathon/evaluation.html"  # Шаблон
        return render(request, template, context)

def info_team(request):
    field = request.GET.get('inputValue')
    data = {
        'response': field,
    }
    return JsonResponse(data)