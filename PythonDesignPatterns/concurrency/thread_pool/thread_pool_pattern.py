from concurrency.thread_pool.person import Person
from concurrency.thread_pool.roller_coaster import RollerCoaster

class ThreadPoolPattern(object):
    """Demonstrates the guarded suspension pattern."""

    def __init__(self):
        self.park_goers = [Person(str(i)) for i in range(100)]
        self.the_runtime_error = RollerCoaster()
        [self.the_runtime_error.add_patron_to_line(person) for person in self.park_goers]

    def demonstrate(self):
        self.the_runtime_error.begin_ride()
