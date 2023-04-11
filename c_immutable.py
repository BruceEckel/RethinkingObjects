# c_immutable.py
# Encapsulation is only required because of mutability
from attrs import frozen  # Or dataclasses

@frozen
class Bob:
    name: str = "Bob"

@frozen
class Immutable:
    n: int
    t: tuple
    b: Bob

def test_immutable():
    immutable = Immutable(42, ("x", "y"), Bob())
    assert (
        repr(immutable)
        == "Immutable(n=42, t=('x', 'y'), b=Bob(name='Bob'))"
    )
    nn = immutable.n
    nn += 1
    _tt = immutable.t
    # 'tuple' object has no attribute 'append':
    # _tt.append('z')
    _b = immutable.b
    # _b.name = "Ralph"  # FrozenInstanceError
    assert (
        repr(immutable)
        == "Immutable(n=42, t=('x', 'y'), b=Bob(name='Bob'))"
    )
