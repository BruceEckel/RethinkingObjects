from attrs import frozen, evolve

@frozen
class A:
  id: chr
  description: str

@frozen
class B:
  count: int
  words: tuple[str]

# Compose by creating subobjects in new struct:
@frozen
class Composed:
  a: A
  b: B

c = Composed(A('x', 'an A'), B(3, ("yellow", "brick", "road")))
print(f"{c = }")
c2 = Composed(A('x', 'another A'), B(3, ("blue", "brick", "road")))
print(f"{c2 = }")
print(c == c, c == c2)
print(c.a.description, c.b.words[0])
c3 = evolve(c2, a=A('z', "this is c3"))
print(f"{c3 = }")
c4 = evolve(c2, b=evolve(c2.b, words=("green", "brick", "road")))
print(f"{c4 = }")
