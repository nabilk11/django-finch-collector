from dataclasses import fields
from pyexpat import model
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse, HttpResponseRedirect # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Player
from django.urls import reverse
from django.contrib.auth.models import User



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
        # query parameter for search
        name = self.request.GET.get("name")
        # if it exists
        if name != None:
            context["players"] = Player.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["players"] = Player.objects.all() # no longer using player list, accessing context from DB
            context["header"] = "ALL PLAYERS"
        return context
        # returning context data from fake players db

# Add player View Class
class Add_Player(CreateView):
    model = Player
    fields = ['name', 'img', 'team', 'height', 'position']
    template_name = "add_player.html"
   # success_url = "/players/" - refactoring success url to details page
    # def get_success_url(self):
    #    return reverse('player_detail', kwargs={'pk': self.object.pk})
    def form_valid(self, form): # occurs after form validation
        self.object = form.save(commit=False)  # save without commiting to the DB
        self.object.user = self.request.user #adding userid
        self.object.save() #saving to db - then redirect 
        return HttpResponseRedirect('/players')

# PLayer Detail View Class
class PlayerDetail(DetailView):
    model = Player
    template_name = "player_detail.html"

# PLayer Update View Class
class PlayerUpdate(UpdateView):
    model = Player
    fields = ['name', 'img', 'team', 'height', 'position']
    template_name = 'player_update.html'
    #success_url = '/players/'
    def get_success_url(self):
       return reverse('player_detail', kwargs={'pk': self.object.pk})

# Player Delete View Class
class PlayerDelete(DeleteView):
    model = Player
    template_name = 'player_delete_confirmation.html'
    success_url = '/players/'

#USER PROFILE PAGE FUNCTION
def profile(request, username):
    user = User.objects.get(username = username)
    players = Player.objects.filter(user = user)
    return render(request, 'profile.html', {'username': username, 'players': players})