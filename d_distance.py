# d_distance.py
from attrs import frozen
from math import sqrt

@frozen
class Point:
    x: int
    y: int

    # "Proper OO", but can't use Point annotation
    def distance_to(self, p2) -> float:
        return sqrt(
            (p2.x - self.x) ** 2 + (p2.y - self.y) ** 2
        )

# Why not this?
def distance(p1: Point, p2: Point) -> float:
    return sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

def test_pythagorean_triple():  # The '3-4-5' Triangle
    p1 = Point(3, 0)
    p2 = Point(0, 4)
    assert p1.distance_to(p2) == 5
    assert distance(p1, p2) == 5
