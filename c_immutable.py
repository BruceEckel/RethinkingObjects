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
    bob: Bob = Bob()

def test_immutable():
    immutable = Immutable(42, ('a', 'b'), {'i': 11, 'j': 12})
    assert repr(immutable) == \
        "Immutable(n=42, t=('a', 'b'), bob={'i': 11, 'j': 12})"
    nn = immutable.n
    nn += 1
    tt = immutable.t
    # ll.append('z')  # 'tuple' object has no attribute 'append'
    b = immutable.bob
    # b.name = "Ralph"  # FrozenInstanceError
    assert repr(immutable) == \
        "Immutable(n=42, t=('a', 'b'), bob={'i': 11, 'j': 12})"
