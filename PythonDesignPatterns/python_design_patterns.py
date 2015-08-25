import sys
from behavioral.memento.memento_pattern import MementoPattern
from behavioral.observer.observer_pattern import ObserverPattern

def main():
    pattern = ObserverPattern()
    pattern.demonstrate()

if __name__ == "__main__":
    main()