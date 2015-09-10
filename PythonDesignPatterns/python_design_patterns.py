import sys

from behavioral.memento.memento_pattern import MementoPattern
from behavioral.observer.observer_pattern import ObserverPattern
from concurrency.guarded_suspension.guarded_suspension_pattern import GuardedSuspensionPattern
from concurrency.thread_pool.thread_pool_pattern import ThreadPoolPattern
from creational.abstract_factory.abstract_factory_pattern import AbstractFactoryPattern
from creational.builder.builder_pattern import BuilderPattern


def main():
    pattern = BuilderPattern()
    pattern.demonstrate()

if __name__ == "__main__":
    main()