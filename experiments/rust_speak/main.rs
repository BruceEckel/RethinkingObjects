//: RethinkingObjects/experiments/rust_speak/main.rs
struct Base {
  eating: String,
  speaking: String,
}

struct Person {
  base: Base,
}
struct Robot {
  base: Base,
}

trait Basic {
  fn eat(&self);
  fn speak(&self);
}

// impl dyn Basic {
//   fn eat(&self) { println!("{}", self.eating); }
//   fn speak(&self) { println!("{}", self.speaking); }
// }

impl Basic for Person {
  fn eat(&self) { println!("{}", self.base.eating); }
  fn speak(&self) { println!("{}", self.base.speaking); }
}

impl Basic for Robot {
  fn eat(&self) { println!("{}", self.base.eating); }
  fn speak(&self) { println!("{}", self.base.speaking); }
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

fn make_person() -> Person {
  Person {
    base: Base {
      eating: String::from("eating pizza"),
      speaking: String::from("blah blah")
    }
  }
}

fn make_robot() -> Robot {
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
