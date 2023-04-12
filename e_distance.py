# e_distance.py
# Generalizing distance() using protocols
from attrs import frozen
from math import sqrt
from typing import Protocol

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

# An explicit adapter:
@frozen
class Adapt(Coord):
    ab: AB  # Composition

    @property
    def x(self):
        return self.ab.a

    @property
    def y(self):
        return self.ab.b

def test_adapt():
    assert distance(Adapt(AB(3, 0)), Adapt(AB(0, 4))) == 5
