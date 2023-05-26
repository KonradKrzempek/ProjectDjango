from django.contrib import admin
from .models import Game, UserGame


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'taken']
    list_filter = ['taken']


@admin.register(UserGame)
class UserGameAdmin(admin.ModelAdmin):
    list_display = ['user', 'game']
    search_fields = ['user__username', 'game__title']

