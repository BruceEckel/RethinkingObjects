# e_distance.py
# Generalizing distance() using protocols
from attrs import frozen
from math import sqrt
from typing import Protocol

class Coord(Protocol):
    x: int
    y: int

def distance(p1: Coord, p2: Coord) -> float:
    return sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

@frozen
class Point(Coord):
    x: int
    y: int

def test_pythagorean_triple():
    assert distance(Point(3, 0), Point(0, 4)) == 5

@frozen
class AB:
    a: int
    b: int

def test_point_adapter():
    p1, p2 = AB(3, 0), AB(0, 4)
    # Point can be used as an adapter:
    assert distance(Point(p1.a, p1.b), Point(p2.a, p2.b)) == 5

# An explicit adapter:
@frozen
class Adapt(Coord):
    ab: AB  # Composition!
    @property
    def x(self): return self.ab.a
    @property
    def y(self): return self.ab.b

def test_adapt():
    assert distance(Adapt(AB(3, 0)), Adapt(AB(0, 4))) == 5
