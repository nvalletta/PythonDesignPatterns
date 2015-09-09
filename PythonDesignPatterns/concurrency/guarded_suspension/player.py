from concurrency.guarded_suspension.coach import Coach
import threading
import sys

class Player(object):
    """Likes to play dodge ball."""

    def __init__(self, name):
        self.name = name

    def throw_balls(self):
        while Coach.game_is_on():
            print(self.name + " throws a ball!\n")
            sys.stdout.flush()

    def start_playing(self):
        while True:
            self.throw_balls()

    def participate(self):
        t = threading.Thread(target=self.start_playing)
        t.start()
        