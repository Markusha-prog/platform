from django.contrib import admin
from .models import Hackathon, File_QR

@admin.register(Hackathon)
class HackathonAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_event', 'end_event', 'representative_case')

admin.site.register(File_QR)