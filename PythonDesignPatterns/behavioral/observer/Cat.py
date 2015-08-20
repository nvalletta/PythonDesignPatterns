from threading import Timer
from behavioral.observer.observable import Observable

class Cat(Observable):
    """description of class"""

    def __init__(self, name):
        Observable.__init__(self)
        self.name = name

    def does_something_cute(self):
        print("Cat flips out!")
        self.notify();

    def be_a_cat(self):
        t = Timer(5, self.does_something_cute)
        t.start()