from creational.abstract_factory.models.gem import Gem
from creational.abstract_factory.models.enchant import Enchant

class Weapon(object):
    """description of class"""

    def __init__(self, enchant_type, gem_type, weapon_type):
        self.enchant = Enchant(enchant_type)
        self.gem = Gem(gem_type)
        self.weapon_type = weapon_type
        self.description = "\n    Enchant: " + str(enchant_type) + "\n    Gem: " + str(gem_type) + "\n    Weapon type: " + str(weapon_type) + "\n"