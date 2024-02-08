# from django.shortcuts import HttpResponse
# from django.shortcuts import render
#
from .models import Game

# from django.shortcuts import render
# from django.views import View

from django.views.generic import ListView

# Create your views here.
# def gameslist(request):
#     return HttpResponse("Hello, world. You're at the gameslist index.")

# def gameslist(request, s0):
#     s1 = request.GET.get('s1', '')
#     return render(
#         request, template_name='gameslist_landing_page.html',
#         context={'adjectives': [s0, s1, 'cool', 'beautiful']}
#     )

# def gameslist(request):
#     return render(
#         request, template_name='games_list_template.html',
#         context={'games': Game.objects.all()}
#     )

# Class-based views

# class GamesListView(View):
#     def get(self, request):
#         return render(
#             request, template_name='games_list_template.html',
#             context={'games': Game.objects.all()}
#         )

# class GamesListView(TemplateView):
#     template_name = 'games_list_template.html'
#     extra_context = {'games': Game.objects.all()}

class GamesListView(ListView):
    template_name = 'games_list_template.html'
    model = Game
