"""
URL configuration for gameslibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.shortcuts import redirect
from gamesplayer.views import gamesplayer, hello_player
from gameslist.views import (
    GamesListCreateView, GamesListView, GamesListUpdateView, GamesListDeleteView
)

from gameslist.models import Genre, Game

admin.site.register(Genre)
admin.site.register(Game)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda req: redirect('gameslist/')),
    path('gameslist/', GamesListView.as_view(), name='gameslist'),
    path('gamesplayer/', hello_player, name='hello_player'),
    path('gameslist/create/', GamesListCreateView.as_view(), name='gameslist_create'),
    path('gameslist/update/<pk>', GamesListUpdateView.as_view(), name='gameslist_update'),
    path('gameslist/delete/<pk>', GamesListDeleteView.as_view(), name='gameslist_delete'),
]
