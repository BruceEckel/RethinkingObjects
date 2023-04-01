# immutable.py
# Encapsulation is only required because of mutability
from attrs import frozen  # Or dataclasses

@frozen
class Bob:
    name: str = "Bob"

@frozen
class Tight:
    x: int
    l: tuple
    bob: Bob = Bob()

def test_tight():
    tight = Tight(42, ('a', 'b'), {'i': 11, 'j': 12})
    assert repr(tight) == \
        "Tight(x=42, l=('a', 'b'), bob={'i': 11, 'j': 12})"
    xx = tight.x
    xx += 1
    ll = tight.l
    # ll.append('z')  # 'tuple' object has no attribute 'append'
    b = tight.bob
    # b.name = "Ralph"  # FrozenInstanceError
    assert repr(tight) == \
        "Tight(x=42, l=('a', 'b'), bob={'i': 11, 'j': 12})"
