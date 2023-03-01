//: RethinkingObjects/experiments/rust_objects2/main.rs

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
  let a = All {
    a: A { description: String::from("hello world") },
    b: B { count: 11 },
    c: C { id: 3 },
  };
  println!("a.description(): {}", a.description());
  println!("a.count(): {}", a.count());
  println!("a.id(): {}", a.id());
}



// impl Basic for Base {
//   fn eat(&self) { println!("{}", self.description); }
//   fn speak(&self) { println!("{}", self.count); }
// }

// struct Person {
//   base: Base,
// }

// struct Robot {
//   base: Base,
// }

// trait BaseDelegator {
//   fn base(&self) -> &Base;
// }

// impl BaseDelegator for Person {
//   fn base(&self) -> &Base {
//     &self.base
//   }
// }

// impl BaseDelegator for Robot {
//   fn base(&self) -> &Base {
//     &self.base
//   }
// }

// impl<T: BaseDelegator> Basic for T {
//   fn eat(&self) {
//     self.base().eat()
//   }
//   fn speak(&self) {
//     self.base().speak()
//   }
// }

// trait Walker {
//   fn walk(&self);
// }

// impl Walker for Person {
//   fn walk(&self) { println!("dumb human walking"); }
// }

// impl Walker for Robot {
//   fn walk(&self) { println!("smart robot rolling"); }
// }

// trait Everything: Basic + Walker {
//   fn do_everything(&self) {  // Default implementation
//     self.eat();
//     self.speak();
//     self.walk();
//   }
// }

// impl Everything for Person {}
// impl Everything for Robot {}

// fn make_person() -> Person { // Constructor
//   Person {
//     base: Base {
//       description: String::from("description pizza"),
//       count: String::from("blah blah")
//     }
//   }
// }

// fn make_robot() -> Robot { // Constructor
//   Robot {
//     base: Base {
//       description: String::from("charging"),
//       count: String::from("beep ping")
//     }
//   }
// }

// fn main() {
//   let person = make_person();
//   let robot = make_robot();
//   let v: Vec<&dyn Everything> = vec![&person, &robot];
//   for e in v.iter() {
//     e.do_everything();
//   }
// }
