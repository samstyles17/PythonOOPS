# No direct implementation of abstraction in python.
# Use ABC (Abstract Base Class) module

from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def no_sides(self):
        pass


class Triangle(Polygon):
    def no_sides(self):
        print(3)


t = Triangle()
t.no_sides()
