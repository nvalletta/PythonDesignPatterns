import sys

class Person(object):
    """Hi, I'm a person."""

    def __init__(self, name):
        self.name = name

    def have_fun(self):
        print(self.name + " is having fun!")
        sys.stdout.flush()
