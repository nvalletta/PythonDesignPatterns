class AbstractPlayerFactory(object):
    """Because Python doesn't have (and doesn't need) 
    a formal Interface contract, the Java-style distinction 
    between abstraction and interface doesn't exist. If 
    someone goes through the effort to define a formal 
    interface, it will also be an abstract class. The 
    only differences would be in the stated intent in 
    the docstring. Java uses interfaces because it 
    doesn't have multiple inheritance.
                          - S. Lott, StackOverflow.com"""

    def create_starting_zone(self):
        raise NotImplementedError("AbstractPlayerFactories must implement create_starting_zone().")

    def create_player(self):
        raise NotImplementedError("AbstractPlayerFactories must implement create_player().")
