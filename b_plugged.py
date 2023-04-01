# plugged.py
from a_encapsulation import Leaky, check_for_leaks
from copy import copy

class Plugged(Leaky):
    def __init__(self, x: int, l: list):
        super().__init__(x, l)

    @property
    def x(self): return self._x

    @property
    def l(self): return self._l.copy()

    @property
    def bob(self): return copy(self._bob)

    # Requires vigilance here & in subclasses:
    def leak(self): return self._bob

def test_leaks():
    before, after = check_for_leaks(Plugged)
    assert before == """
Plugged:
    x: 42
    l: ['a', 'b']
    bob: Bob
"""
    assert after == """
Plugged:
    x: 42
    l: ['a', 'b']
    bob: Bob
"""
