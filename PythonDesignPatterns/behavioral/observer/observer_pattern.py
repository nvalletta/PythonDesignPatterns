from behavioral.observer.human import Human
from behavioral.observer.cat import Cat

class ObserverPattern(object):
    """Demonstrates the observer pattern."""

    def __init__(self):
        self.nora = Human("Nora")
        self.cat = Cat("Mona")
        self.nora.adopt_cat(self.cat)
        
    def demonstrate(self):
        self.cat.be_a_cat()