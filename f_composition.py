from attrs import frozen, evolve

@frozen
class A:
    id: chr
    desc: str

@frozen
class B:
    n: int
    words: tuple[str]

# Compose by creating subobjects in new struct:
@frozen
class Composed:
    a: A
    b: B

def f(c: Composed) -> Composed:
    return evolve(c, b=evolve(c.b, words=("no", "duh")))

def test_composed():
    c = Composed(A('x', 'A1'), B(3, ("oh", "wow")))
    assert repr(c) == \
    "Composed(a=A(id='x', desc='A1'), b=B(n=3, words=('oh', 'wow')))"
    c2 = f(c)
    assert repr(c2) == \
    "Composed(a=A(id='x', desc='A1'), b=B(n=3, words=('no', 'duh')))"
    assert c2 != c
    print("Does this show up?")
    # assert c2 < c
    # c2 = Composed(A('x', 'also A'), B(3, ("too", "much")))
    # print(f"{c2 = }")
    # print(c == c, c == c2)
    # print(c.a.description, c.b.words[0])
    # c3 = evolve(c2, a=A('z', "this is c3"))
    # print(f"{c3 = }")
    # c4 = evolve(c2, b=evolve(c2.b, words=("green", "brick", "road")))
    # print(f"{c4 = }")
