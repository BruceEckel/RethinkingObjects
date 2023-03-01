//: RethinkingObjects/experiments/rust_objects2/main.rs
// Composition

struct A {
  description: String,
}

struct B {
  count: i32,
}

struct C {
  id: i8,
}

// Compose by creating subobjects in new struct:
struct All {
  a: A,
  b: B,
  c: C,
}

trait Info {
  fn description(&self) -> &String;
  fn count(&self) -> i32;
  fn id(&self) -> i8;
}

impl Info for All {
  fn description(&self) -> &String { &self.a.description }
  fn count(&self) -> i32 { self.b.count }
  fn id(&self) -> i8 { self.c.id }
}

fn main() {
  let x = All {
    a: A { description: String::from("hello world") },
    b: B { count: 11 },
    c: C { id: 3 },
  };
  println!("x.description(): {}", x.description());
  println!("x.count(): {}", x.count());
  println!("x.id(): {}", x.id());
}
