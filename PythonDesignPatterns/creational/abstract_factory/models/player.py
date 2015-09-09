import sys

class Player(object):
    """description of class"""

    def __init__(self, weapon, armor):
        self.weapon = weapon
        self.armor = armor

    def print_details(self):
        print("Weapon: {" + self.weapon.description + "}\nArmor: {" + self.armor.description + "}")
        sys.stdout.flush()