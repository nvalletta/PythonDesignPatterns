from creational.abstract_factory.models.gem import Gem
from creational.abstract_factory.models.enchant import Enchant

class Weapon(object):
    """description of class"""

    def __init__(self, enchant_type, gem_type, weapon_type):
        self.enchant = Enchant(enchant_type)
        self.gem = Gem(gem_type)
        self.weapon_type = weapon_type
        self.description = "Enchant: " + str(enchant_type) + "\nGem: " + str(gem_type) + "\n Weapon type: " + str(weapon_type)