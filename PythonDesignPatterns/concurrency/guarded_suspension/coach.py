import sched, time
import sys

class Coach(object):

    _play_ball = False

    @staticmethod
    def game_is_on():
        return Coach._play_ball

    @staticmethod
    def toggle_game_play():
        if Coach._play_ball:
            Coach._play_ball = False
            print("Stop playing.")
        else:
            Coach._play_ball = True
            print("If you can dodge a wrench, you can dodge a ball! Game on!")
        sys.stdout.flush()

    def __init__(self):
        Coach._play_ball = False

    @staticmethod
    def coach_the_game():
        s = sched.scheduler(time.time, time.sleep)
        s.enter(5, 1, Coach.toggle_game_play)
        s.run()
