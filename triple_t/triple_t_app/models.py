from django.db import models

# Create your models here.
class State(models.Model):
    [Win, In progress, Tie]

class Piece(models.Model):
    piece = [X, O, NULL]

class Box(models.Model):
    board = models.ForeignKey("Board", on_delete=models.PROTECT)
    piece = models.ForeignKey("Piece", on_delete=models.PROTECT)

class Board(models.Model):
    game = models.ForeignKey("Game", on_delete=models.RESTRICT)

class Game(models.Model):
    state = models.ForeignKey("State", on_delete=models.PROTECT)
    winner = models.ForeignKey("Piece", on_delete=models.PROTECT)