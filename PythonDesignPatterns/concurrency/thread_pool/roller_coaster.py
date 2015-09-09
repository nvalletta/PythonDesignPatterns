from concurrency.thread_pool.person import Person
from concurrent import futures

class RollerCoaster(object):
    """Represents a super fun roller coaster."""

    def __init__(self):
        self.threads = list()
        self.patron_line = list()
        self.max_capacity = 10
        self.threadPool = futures.ThreadPoolExecutor(self.max_capacity)

    def add_patron_to_line(self, patron):
        self.patron_line.append(patron)
        self.threads.append(self.threadPool.submit(patron.have_fun))

    def begin_ride(self):
        futures.wait(self.threads, return_when=futures.ALL_COMPLETED)
