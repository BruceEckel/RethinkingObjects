//: RethinkingObjects/experiments/rust_objects1/main.rs

struct Base {
  description: String,
  count: i32,
}

trait Info {
  fn description(&self) -> &String;
  fn count(&self) -> i32;
}

impl Info for Base {
  fn description(&self) -> &String { &self.description }
  fn count(&self) -> i32 { self.count }
}

trait InfoB {
  fn summary_b(&self);
}

impl InfoB for Base {
  fn summary_b(&self) {
    println!("summary_b: {}: {}", self.description, self.count);
  }
}

trait InfoC {
  fn summary_c(&self);
}

impl<T: Info> InfoC for T {
  fn summary_c(&self) {
    println!("summary_c: {}: {}", self.description(), self.count());
  }
}

fn main() {
  let b = Base {
    description: String::from("hello world"),
    count: 11,
  };
  b.summary_b();
  b.summary_c();
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
