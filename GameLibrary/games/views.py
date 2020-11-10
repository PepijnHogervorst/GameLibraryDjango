from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Game

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'games/index.html'
    context_object_name = 'latest_games_list'

    def get_queryset(self):
        return Game.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Game
    template_name = 'games/detail.html'
