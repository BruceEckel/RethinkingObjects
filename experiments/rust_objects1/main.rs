//: RethinkingObjects/experiments/rust_objects1/main.rs
// Basic Rust "objects"

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

impl InfoB for Base {  // Notice Base is a struct
  fn summary_b(&self) {
    println!("summary_b(): {}: {}", self.description, self.count);
  }
}

trait InfoC {
  fn summary_c(&self);
}

impl<T: Info> InfoC for T {  // T must be a trait, not a struct (!)
  fn summary_c(&self) {
    println!("summary_c(): {}: {}", self.description(), self.count());
  }
}  // Notice: No explicit InfoC for Base!

// Or you could do it like this -- but not at the same time (conflict):
// impl<T: InfoB> InfoC for T {
//   fn summary_c(&self) {
//     self.summary_b();
//   }
// }


fn main() {
  let b = Base {
    description: String::from("hello world"),
    count: 11,
  };
  println!("b.description(): {}", b.description());
  b.summary_b();
  b.summary_c();
}
