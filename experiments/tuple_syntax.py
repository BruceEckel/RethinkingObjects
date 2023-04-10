def f() -> tuple[str, float]:
    return "pi", 3.14159

def test_tuple_plain():
    s, p = f()
    assert s == "pi"
    assert p == 3.14159

def test_tuple_parenthesized():
    (s, p) = f()
    assert s == "pi"
    assert p == 3.14159
