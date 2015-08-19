import threading

class Cat(behavioral.observer.event):
    """description of class"""

    def __init__(self, name):
        self.name = name

    def does_something_cute(self):
        print("Cat flips out!")
        super(Observable, self).notify();

    def be_a_cat(self):
        t = Timer(5, does_something_cute)