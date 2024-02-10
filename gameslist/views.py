# from django.shortcuts import HttpResponse
# from django.shortcuts import render
#

# from django.shortcuts import render
# from django.views import View

from logging import getLogger

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, TemplateView, UpdateView, DeleteView
)

from .models import Game
from gameslist.forms import GameForm

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

LOGGER = getLogger()


class GamesListView(TemplateView):
    template_name = 'games_list_template.html'
    extra_context = {'games': Game.objects.all()}


class GamesListCreateView(CreateView):
    template_name = 'gameslist_form.html'
    form_class = GameForm
    success_url = reverse_lazy('gameslist')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data')
        return super().form_invalid(form)

    # def form_valid(self, form):
    #     # form.instance.author = self.request.user
    #     return super().form_valid(form)

    # def get_success_url(self):
    #     return '/gameslist/'


class GamesListUpdateView(UpdateView):
    template_name = 'gameslist_form.html'
    model = Game
    form_class = GameForm
    success_url = reverse_lazy('gameslist')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data while updating a movie.')
        return super().form_invalid(form)


class GamesListDeleteView(DeleteView):
    template_name = 'gameslist_confirm_delete.html'
    model = Game
    success_url = reverse_lazy('gameslist')
