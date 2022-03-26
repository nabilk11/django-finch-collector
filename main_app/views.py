from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Player

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


# INDV Player
# class Player:
#     def __init__(self, name, team, height, position):
#         self.name = name
#         self.team = team
#         self.height = height
#         self.position = position

# # initial player DB
# players = [
#     Player("Lebron James", "Lakers", 81, "F" ),
#     Player("Carmelo Anthony", "Lakers", 80, "F" ),
#     Player("Kevin Durant", "Nets", 83, "F" ),
#     Player("Kyrie Irving", "Nets", 74, "G" ),
# ]

# Players List
class PlayersList(TemplateView):
    template_name = "players.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["players"] = Player.objects.all() # no longer using player list, accessing context from DB
        return context
        # returning context data from fake players db

