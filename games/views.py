from django.shortcuts import render, redirect
from .models import Game, UserGame
from django.db.models import Q

def game_view(request):
    query = request.GET.get('search')
    if query:
        games = Game.objects.filter(Q(title__icontains=query))
    else:
        games = Game.objects.all()

    # Check if the logged-in user already owns each game
    if request.user.is_authenticated:
        owned_games = UserGame.objects.filter(user=request.user).values_list('game_id', flat=True)
        for game in games:
            game.is_owned = game.id in owned_games

    context = {'games': games}
    return render(request, 'game_view.html', context)


def game_search(request):
    query = request.GET.get('q')
    if not query:
        games = Game.objects.all()
    else:
        games = Game.objects.filter(title__icontains=query)

        # Check if the logged-in user already owns each game
    if request.user.is_authenticated:
        owned_games = UserGame.objects.filter(user=request.user).values_list('game_id', flat=True)
        for game in games:
            game.is_owned = game.id in owned_games

    context = {'games': games}
    return render(request, 'game_search.html', context)


def my_games(request):
    user_games = UserGame.objects.filter(user=request.user)
    games = [user_game.game for user_game in user_games]
    return render(request, 'my_games.html', {'games': games})

def buy_game(request, game_id):
    game = Game.objects.get(id=game_id)
    user_game = UserGame(user=request.user, game=game)
    user_game.save()
    return redirect('my_games')