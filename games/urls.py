from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_view, name='game_view'),
    path('search/', views.game_search, name='game_search'),
    path('my-games/', views.my_games, name='my_games'),
    path('buy/<int:game_id>/', views.buy_game, name='buy_game'),
]
