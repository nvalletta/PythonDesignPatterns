from creational.abstract_factory.factories.mage_factory import MageFactory
from creational.abstract_factory.factories.warrior_factory import WarriorFactory
import sys

class AbstractFactoryPattern(object):
    """description of class"""

    def __init__(self):
        pass


    def get_factory(self):
        player_type = input("What class would you like to be?")
        factory = None

        if str(player_type).lower() == "mage":
            factory = MageFactory()
        if str(player_type).lower() == "warrior":
            factory = WarriorFactory()

        return factory


    def demonstrate(self):
        self.factory = self.get_factory()

        while self.factory == None:
            print("Hey! That's not a valid class...\n")
            sys.stdout.flush()
            self.factory = self.get_factory()

        player = self.factory.create_player()
        zone = self.factory.create_starting_zone()

        player.print_details()
        zone.print_details()