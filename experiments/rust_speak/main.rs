//: RethinkingObjects/experiments/rust_speak/main.rs
struct Base {
  eating: String,
  speaking: String,
}

trait Basic {
  fn eat(&self);
  fn speak(&self);
}

impl Basic for Base {
  fn eat(&self) { println!("{}", self.eating); }
  fn speak(&self) { println!("{}", self.speaking); }
}

struct Person {
  base: Base,
}

struct Robot {
  base: Base,
}

impl Basic for Person {
  fn eat(&self) { self.base.eat(); }
  fn speak(&self) { self.base.speak(); }
}

impl Basic for Robot {
  fn eat(&self) { self.base.eat(); }
  fn speak(&self) { self.base.speak(); }
}

trait Walker {
  fn walk(&self);
}

impl Walker for Person {
  fn walk(&self) { println!("dumb human walking"); }
}

impl Walker for Robot {
  fn walk(&self) { println!("smart robot rolling"); }
}

trait Everything: Basic + Walker {
  fn do_everything(&self) {  // Default implementation
    self.eat();
    self.speak();
    self.walk();
  }
}

impl Everything for Person {}
impl Everything for Robot {}

fn make_person() -> Person { // Constructor
  Person {
    base: Base {
      eating: String::from("eating pizza"),
      speaking: String::from("blah blah")
    }
  }
}

fn make_robot() -> Robot { // Constructor
  Robot {
    base: Base {
      eating: String::from("charging"),
      speaking: String::from("beep ping")
    }
  }
}

fn main() {
  let person = make_person();
  let robot = make_robot();
  let v: Vec<&dyn Everything> = vec![&person, &robot];
  for e in v.iter() {
    e.do_everything();
  }
}
