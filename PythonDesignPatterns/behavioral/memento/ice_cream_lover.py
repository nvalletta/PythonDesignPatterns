from behavioral.memento.ice_cream_order import IceCreamOrder
from behavioral.memento.ice_cream_memento import IceCreamMemento

class IceCreamLover(object):
    """A lover of ice creams is a thing who loves the ice cream."""

    def __init__(self, name="Lover of the ice creams"):
        self.name = name
        self.ice_cream_order = IceCreamOrder()
        self.ice_cream_memento = IceCreamMemento()

    def save_order_to_memento(self):
        self.ice_cream_memento.save(self.ice_cream_order)

    def restore_order_from_memento(self):
        self.ice_cream_memento.restore(self.ice_cream_order)

    def print_ice_cream_order(self):
        print(self.ice_cream_order)
