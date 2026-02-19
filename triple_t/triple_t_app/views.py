from django.shortcuts import render
from django.views import generic
from .models import Game, Board, Box

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_games = Game.objects.all().count()
    num_boards = Board.objects.all().count()
    num_boxes = Box.objects.all().count()

    context = {
        'num_games': num_games,
        'num_boards': num_boards,
        'num_boxes': num_boxes,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)