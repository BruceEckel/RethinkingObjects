# b_plugged.py
from a_encapsulation import Leaky, check_for_leaks
from copy import copy

class Plugged(Leaky): # Only to reduce code here
    def __init__(self, n: int, lst: list):
        super().__init__(n, lst)

    @property
    def x(self): return self._x

    @property # Decouple by copying:
    def lst(self): return self._lst.copy()

    @property # Ditto:
    def bob(self): return copy(self._bob)

    # Can re-leak here & in subclasses:
    def leak(self): return self._bob

def test_leaks():
    before, after = check_for_leaks(Plugged)
    assert before == """
Plugged:
    n: 42
    lst: ['a', 'b']
    bob: Bob
"""
    assert after == """
Plugged:
    n: 42
    lst: ['a', 'b']
    bob: Bob
"""
