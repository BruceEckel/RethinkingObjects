# encapsulation.py
from textwrap import dedent

class Bob:
    def __init__(self):
        self.name = "Bob"
    def __repr__(self): return f"{self.name}"

class Leaky:
    def __init__(self, x: int, l: list):
        self._x: int = x
        self._l: list = l  # True for dicts too
        self._bob: Bob = Bob()

    @property
    def x(self): return self._x

    @property
    def l(self): return self._l

    @property
    def bob(self): return self._bob

    def __repr__(self):
        return dedent(f"""\
        {type(self).__name__}:
            x: {self._x}
            l: {self._l}
            bob: {self._bob}""")

    # ... Also might need comparison, hashcode etc.

def test_for_leaks(Klass):
    obj = Klass(42, ['a', 'b'])
    print(obj)
    xx = obj.x
    xx += 1
    ll = obj.l
    ll.append('z')
    b = obj.bob
    b.name = "Ralph"
    print(obj)

if __name__ == "__main__":
    test_for_leaks(Leaky)
"""
Leaky:
    x: 42
    l: ['a', 'b']
    bob: Bob
Leaky:
    x: 42
    l: ['a', 'b', 'z']
    bob: Ralph
"""
