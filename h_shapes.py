import math
from typing import Union, List
from attrs import frozen

@frozen
class Rectangle:
    length: float
    width: float

@frozen
class Circle:
    radius: float

def area(shape: Rectangle | Circle) -> float:
    match shape:
        case Rectangle(length=l, width=w):
            return l * w
        case Circle(radius=r):
            return math.pi * r ** 2

def test_shapes() -> None:
    r = math.sqrt(4.0 / math.pi)
    shapes: List[Rectangle | Circle] = [Circle(r), Rectangle(3.0, 4.0)]
    assert round(area(shapes[0])) == 4
    assert area(shapes[1]) == 12
