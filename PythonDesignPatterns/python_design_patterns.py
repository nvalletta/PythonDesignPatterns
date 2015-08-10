import sys
from behavioral.memento.memento_pattern import MementoPattern
from builtins import print

def main():
    print("It works!")
    pattern = MementoPattern()
    pattern.demonstrate()

if __name__ == "__main__":
    main()