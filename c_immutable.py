# c_immutable.py
# Encapsulation is only required because of mutability
from attrs import frozen  # Or dataclasses

@frozen
class Bob:
    name: str = "Bob"

@frozen
class Immutable:
    x: int
    l: tuple
    bob: Bob = Bob()

def test_immutable():
    immutable = Immutable(42, ('a', 'b'), {'i': 11, 'j': 12})
    assert repr(immutable) == \
        "Immutable(x=42, l=('a', 'b'), bob={'i': 11, 'j': 12})"
    xx = immutable.x
    xx += 1
    ll = immutable.l
    # ll.append('z')  # 'tuple' object has no attribute 'append'
    b = immutable.bob
    # b.name = "Ralph"  # FrozenInstanceError
    assert repr(immutable) == \
        "Immutable(x=42, l=('a', 'b'), bob={'i': 11, 'j': 12})"
