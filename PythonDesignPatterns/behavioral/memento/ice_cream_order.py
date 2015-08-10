class IceCreamOrder(object):
    """description of class"""

    def __init__(self):
        self.flavor = "Vanilla"
        self.toppings = ""
        self.scoops = 2
        self.is_in_a_cone = False

    def __str__(self):
        return "Flavor: %s, Toppings: %s, Scoops: %d, Is in a cone: %r" % (self.flavor,
                                                                           self.toppings,
                                                                           self.scoops,
                                                                           self.is_in_a_cone)