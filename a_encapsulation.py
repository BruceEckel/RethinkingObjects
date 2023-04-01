# a_encapsulation.py
from textwrap import dedent

class Bob:
    def __init__(self):
        self.name = "Bob"
    def __repr__(self): return f"{self.name}"

class Leaky:
    def __init__(self, x: int, l: list):
        self._x: int = x
        self._l: list = l
        self._bob: Bob = Bob()

    @property
    def x(self): return self._x

    @property
    def l(self): return self._l

    @property
    def bob(self): return self._bob

    def __repr__(self):
        return dedent(f"""
        {type(self).__name__}:
            x: {self._x}
            l: {self._l}
            bob: {self._bob}
        """)

    # ... Also might need comparison, hashcode etc.

def check_for_leaks(Klass):
    obj = Klass(42, ['a', 'b'])
    before = repr(obj)
    xx = obj.x
    xx += 1
    ll = obj.l
    ll.append('z')
    b = obj.bob
    b.name = "Ralph"
    return before, repr(obj)

def test_leaks():
    before, after = check_for_leaks(Leaky)
    assert before == """
Leaky:
    x: 42
    l: ['a', 'b']
    bob: Bob
"""
    assert after == """
Leaky:
    x: 42
    l: ['a', 'b', 'z']
    bob: Ralph
"""
