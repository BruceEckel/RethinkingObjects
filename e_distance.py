# e_distance.py
# Generalizing distance() using protocols
from math import sqrt
from typing import Protocol
from attrs import field, frozen

class Coord(Protocol):
    x: int
    y: int

def distance(c1: Coord, c2: Coord) -> float:
    return sqrt((c2.x - c1.x) ** 2 + (c2.y - c1.y) ** 2)

@frozen
class Point(Coord):
    x: int
    y: int

def test_pythagorean_triple():
    assert distance(Point(3, 0), Point(0, 4)) == 5

# Suppose you are handed this non-Coord class:
@frozen
class AB:
    a: int
    b: int

def test_point_adapter():
    ab1, ab2 = AB(3, 0), AB(0, 4)
    # Point can be used as an adapter:
    d = distance(Point(ab1.a, ab1.b), Point(ab2.a, ab2.b))
    assert d == 5

# An adapter class:
@frozen
class Adapt(Coord):
    ab: AB  # Composition
    x: int = field()
    @x.default
    def dx(self): return self.ab.a
    y: int = field()
    @y.default
    def dy(self): return self.ab.b

def test_adapt_class():
    assert distance(Adapt(AB(3, 0)), Adapt(AB(0, 4))) == 5
