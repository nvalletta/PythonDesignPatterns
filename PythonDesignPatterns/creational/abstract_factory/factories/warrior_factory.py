from creational.abstract_factory.factories.abstract_player_factory import AbstractPlayerFactory
from creational.abstract_factory.models.weapon import Weapon
from creational.abstract_factory.models.armor import Armor
from creational.abstract_factory.models.player import Player
from creational.abstract_factory.models.starting_zone import StartingZone


class WarriorFactory(AbstractPlayerFactory):
    """description of class"""

    def __init__(self):
        self.gem_type = "Fiery Red Gem"
        self.enchant_type = "+ Angry-hate-swingysword Power"
        self.weapon_type = "Sword"
        self.armor_type = "Plate"
        self.starting_zone_type = "In a crowded city."

    def create_player(self):
        weapon = Weapon(self.enchant_type, self.gem_type, self.weapon_type)
        armor = Armor(self.enchant_type, self.gem_type, self.armor_type)
        return Player(weapon, armor)

    def create_starting_zone(self):
        return StartingZone(self.starting_zone_type)
