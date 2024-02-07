from django.shortcuts import HttpResponse


# Create your views here.
def gamesplayer(request):
    return HttpResponse("Hello, world. You're at the gamesplayer index.")


# First method
# def hello_player(request, player):
#     return HttpResponse(f"Hello, {player}. You're at the gamesplayer index.")

# Second method
def hello_player(request):
    s = request.GET.get('s', '')
    if not s:
        s = 'Player'
    return HttpResponse(f"Hello, {s}. You're at the gamesplayer index.")
