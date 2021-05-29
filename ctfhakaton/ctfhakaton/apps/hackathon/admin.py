from django.contrib import admin
from .models import Hackathon

@admin.register(Hackathon)
class HackathonAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_event', 'end_event', 'representative_case')