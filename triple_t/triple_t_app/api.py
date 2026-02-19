# ninja imports
from ninja import NinjaAPI, ModelSchema
from ninja.pagination import paginate, PageNumberPagination

# django imports
from django.shortcuts import get_object_or_404

# local imports
from .models import Game, Board, Box

api = NinjaAPI()

class GameSchema(ModelSchema):
    class Meta:
        model = Game
        fields = "__all__"

# Create your views here.
@api.post("game/")
def create_game(request):
    game_obj = Game.objects.create()

    for i in range(9):
        curr_board = Board.objects.create(game=game_obj, position=i)
        for j in range(9):
            curr_box = Box.objects.create(board=curr_board, position=j)
            curr_box.save()
        curr_board.save()
    game_obj.save()

    return 200, {"message": f"Game #{game_obj.id} created."}

@api.get("game/", response=list[GameSchema])
@paginate(PageNumberPagination)
def get_games(request):
    return Game.objects.all()


@api.delete("game/{id}")
def delete_game(request, id):
    game_obj = get_object_or_404(Game, id=id)
    game_obj.delete()
    return 200, {"message": "Game deleted."}



@api.get("game/{id}")
def game_view(request, id):
    return {"game_id": id}

#def check_win(request, game_id):
#  winning_combinations = [ [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6] ]
#  for combination in winning_combinations:
# check if boxes for combo values are same, return type if same
#