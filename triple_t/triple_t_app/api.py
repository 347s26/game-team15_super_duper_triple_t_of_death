from ninja import NinjaAPI, Schema
from django.shortcuts import render
from .models import Game, Board, Box

api = NinjaAPI()

# Create your views here.
@api.post("/create")
def create_game(request):
    game_obj = Game.objects.create()

    for i in range(9):
        curr_board = Board.objects.create(game=game_obj, position=i)
        for j in range(9):
            curr_box = Box.objects.create(board=curr_board, position=j)
            curr_box.save()
        curr_board.save()
    game_obj.save()

    return {"message": "Game created"}


@api.get("/game/{game_id}")
def game_view(request, game_id):
    return {"game_id": game_id}

#def check_win(request, game_id):
#  winning_combinations = [ [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6] ]
#  for combination in winning_combinations:
# check if boxes for combo values are same, return type if same
#