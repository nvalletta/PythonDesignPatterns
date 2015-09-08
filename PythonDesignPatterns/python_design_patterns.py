import sys
from behavioral.memento.memento_pattern import MementoPattern
from behavioral.observer.observer_pattern import ObserverPattern
from concurrency.guarded_suspension.guarded_suspension_pattern import GuardedSuspensionPattern

def main():
    pattern = GuardedSuspensionPattern()
    pattern.demonstrate()

if __name__ == "__main__":
    main()