import sys
import time

class Person(object):
    """Hi, I'm a person."""

    def __init__(self, name):
        self.name = name

    def have_fun(self):
        time.sleep(5)
        print(self.name + " is having fun!\n")
        sys.stdout.flush()
