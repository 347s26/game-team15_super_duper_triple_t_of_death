from ninja import Schema
from .models import Game

class GameSchema(Schema):
    class Meta:
        model = Game
        fields = "__all__"

