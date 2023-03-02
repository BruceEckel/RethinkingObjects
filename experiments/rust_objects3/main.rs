//: RethinkingObjects/experiments/rust_objects3/main.rs
// Polymorphism

struct Base {
  description: String,
}

trait Show {
  fn show(&self);
}

impl Show for Base {
  fn show(&self) {
    println!("show() for {:?}", self.description);
  }
}

struct Derived {
  base: Base,
  count: i32,
}

impl Show for Derived {
  fn show(&self) {
    println!("show() for {:?}, {:?}", self.base.description, self.count);
  }
}

struct Other {
  id: i8,
}

impl Show for Other {
  fn show(&self) {
    println!("show() for Other: {:?}", self.id);
  }
}

fn main() {
  let b = Base {
    description: String::from("Base"),
  };
  let d = Derived {
    base: Base { description: String::from("Derived") },
    count: 11,
  };
  let o = Other { id: 47 };
  let v: Vec<&dyn Show> = vec![&b, &d, &o];
  for e in v.iter() {
    e.show();
  }
}

