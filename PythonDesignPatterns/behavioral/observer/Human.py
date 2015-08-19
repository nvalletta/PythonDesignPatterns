import behavioral.observer.cat

class Human(object):
    """description of class"""

    def __init__(self, name):
        self.name = name

    def take_a_picture(self):
        print(name + " takes a picture of " + cat.name)

    def adopt_cat(self, cat):
        self.cat = cat
        self.cat.observe(take_a_picture)