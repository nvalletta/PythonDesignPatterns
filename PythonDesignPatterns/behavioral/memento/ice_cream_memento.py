import copy

class IceCreamMemento(object):
    """description of class"""

    def save(self, obj, deep = False):
        self.state = (copy.copy if deep else copy.deepcopy)(obj.__dict__)

    def restore(self, obj):
        obj.__dict__ = self.state