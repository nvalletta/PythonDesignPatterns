import threading
from behavioral.observer.event import Event

class Observable(object):
    """An observable thing."""

    def __init__(self):
        self.callbacks = []

    def observe(self, callback):
        self.callbacks.append(callback)

    def unobserve(self, callback):
        self.callbacks.remove(callback)

    def notify(self):
        e = Event()
        e.source = self

        for fn in self.callbacks:
            fn()
            # If we wanted to notify of the
            # event itself: fn(e)
