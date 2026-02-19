from django.db import models
import uuid

GAME_STATUS = (
    ('Not started', 'not started'),
    ('In Progress', 'in progress'),
    ('Finished', 'finished'),
)

PIECES = (
    ("x", "player 1"),
    ("o", "player 2"),
    ("empty", "non played")
)

class Box(models.Model):
    board = models.ForeignKey("Board", on_delete=models.CASCADE)
    piece = models.CharField(
        max_length=255,
        choices=PIECES,
        blank=False,
        default='empty',
        help_text='Pieces per box'
    )
    position = models.IntegerField(choices=[(i, str(i)) for i in range(1, 10)], default=1)

    def __str__(self):
        return f"Box: {self.position} Board: {self.board.id} Game: {self.board.game.id} Piece: {self.piece}"

class Board(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    position = models.IntegerField(choices=[(i, str(i)) for i in range(1, 10)], default=1)
    status = models.CharField(
        max_length=255,
        choices=GAME_STATUS,
        blank=False,
        default='n',
        help_text='Game Status',
    )

    def __str__(self):
        return f"Board: {self.position} Game: {self.game.id} Status: {self.status}"
    

class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    winner = models.CharField(
        max_length=5,
        choices=PIECES,
        blank=False,
        default='empty',
        help_text='Winner of the game'
    )

    status = models.CharField(
        max_length=255,
        choices=GAME_STATUS,
        blank=False,
        default='Not started',
        help_text='Game Status',
    )
    
    def __str__(self):
        return f"{self.id}: {self.status}"