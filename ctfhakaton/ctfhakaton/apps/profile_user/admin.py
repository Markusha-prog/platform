from django.contrib import admin
from .models import Profile, Group, Team, Tag

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'verification')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('group',)}
    search_fields = ['group']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('team_name',)}
    search_fields = ['team_name', 'team_verification']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['tag_name']