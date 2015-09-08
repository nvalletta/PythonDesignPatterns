from concurrency.guarded_suspension.player import Player
from concurrency.guarded_suspension.coach import Coach

class GuardedSuspensionPattern(object):
    """Demonstrates the guarded suspension pattern."""

    def __init__(self):
        self.player1 = Player("Player1")
        self.player2 = Player("Player2")
        self.player3 = Player("Player3")
        self.coach = Coach()

    def demonstrate(self):
        self.coach.coach_the_game()
        self.player1.participate()
        self.player2.participate()
        self.player3.participate()
        self.coach.coach_the_game()
