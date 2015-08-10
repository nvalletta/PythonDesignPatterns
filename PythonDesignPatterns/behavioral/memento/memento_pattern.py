from behavioral.memento.ice_cream_lover import IceCreamLover

class MementoPattern(object):
    """description of class"""

    def __init__(self):
        self.nora = IceCreamLover("Nora")
        
    def demonstrate(self):
        self.nora.ice_cream_order.flavor = "PlayDoh"
        self.nora.save_order_to_memento()
        self.nora.ice_cream_order.flavor = "Feet"
        self.nora.restore_order_from_memento()
        self.nora.print_ice_cream_order()