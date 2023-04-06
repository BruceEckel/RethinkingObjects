import math
from typing import List

class Shape:
    def area(self) -> float: ...

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
    def area(self) -> float:
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    def area(self) -> float:
        return math.pi * self.radius ** 2

def test_shapes() -> None:
    r = math.sqrt(4.0 / math.pi)
    shapes: List[Shape] = [Circle(r), Rectangle(3.0, 4.0)]
    assert round(shapes[0].area()) == 4
    assert shapes[1].area() == 12
