# f_composition.py
from attrs import frozen, evolve

@frozen
class A:
    id: str
    desc: str

@frozen
class B:
    n: int
    words: tuple[str, ...]

@frozen
class Composed:
    a: A  # Create subobjects in new struct
    b: B

def make_new_from(c: Composed) -> Composed:
    return evolve(c, b=evolve(c.b, words=("no", "duh")))

c = Composed(A('x', 'A1'), B(3, ("oh", "wow")))  # "Safe global"

def test_composed():
    assert repr(c) == \
    "Composed(a=A(id='x', desc='A1'), b=B(n=3, words=('oh', 'wow')))"

def test_evolve():
    c2 = make_new_from(c)
    assert repr(c2) == \
    "Composed(a=A(id='x', desc='A1'), b=B(n=3, words=('no', 'duh')))"
    assert c2 != c # Basic comparison

def test_dict_key():
    d = {c: 'The value'}
    assert str(d[c]) == 'The value'
