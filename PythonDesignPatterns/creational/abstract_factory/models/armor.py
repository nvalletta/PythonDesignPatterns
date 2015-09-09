from creational.abstract_factory.models.gem import Gem
from creational.abstract_factory.models.enchant import Enchant

class Armor(object):
    """description of class"""

    def __init__(self, enchant_type, gem_type, armor_type):
        self.enchant = Enchant(enchant_type)
        self.gem = Gem(gem_type)
        self.armor_type = armor_type
        self.description = "Enchant: " + str(enchant_type) + "\nGem: " + str(gem_type) + "\n Armor type: " + str(armor_type)