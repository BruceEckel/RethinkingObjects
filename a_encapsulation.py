# a_encapsulation.py
from textwrap import dedent

class Bob:
    def __init__(self):
        self._name = "Bob"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    def __repr__(self): return f"{self._name}"

class Leaky:
    def __init__(self, n: int, lst: list):
        self._n: int = n
        self._lst: list = lst
        self._bob: Bob = Bob()

    @property
    def n(self) -> int:
        return self._n

    @property
    def lst(self) -> list:
        return self._lst

    @property
    def bob(self) -> Bob:
        return self._bob

    def __repr__(self):
        return dedent(f"""
        {type(self).__name__}:
            n: {self._n}
            lst: {self._lst}
            bob: {self._bob}
        """)

    # ... Also might need comparison, hashcode etc.

def check_for_leaks(klass):
    obj = klass(42, ["a", "b"])
    before = repr(obj)
    nn = obj.n
    nn += 1
    lst = obj.lst
    lst.append("z")
    b = obj.bob
    b.name = "Ralph"
    return before, repr(obj)

def test_leaks():
    before, after = check_for_leaks(Leaky)
    assert before == """
Leaky:
    n: 42
    lst: ['a', 'b']
    bob: Bob
"""
    assert after == """
Leaky:
    n: 42
    lst: ['a', 'b', 'z']
    bob: Ralph
"""
