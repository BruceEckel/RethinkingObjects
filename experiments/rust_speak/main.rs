//: src/rust/inheritance/src/main.rs
struct Person {
  eating: String,
  speaking: String
}
struct Robot {
  eating: String,
  speaking: String
}

trait Base {
  fn eat(&self);
  fn speak(&self);
}

impl Base for Person {
  fn eat(&self) { println!("{}", self.eating); }
  fn speak(&self) { println!("{}", self.speaking); }
}

impl Base for Robot {
  fn eat(&self) { println!("{}", self.eating); }
  fn speak(&self) { println!("{}", self.speaking); }
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

trait Everything: Base + Walker {
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
    eating: String::from("eating pizza"),
    speaking: String::from("blah blah")
  }
}

fn make_robot() -> Robot {
  Robot {
    eating: String::from("charging"),
    speaking: String::from("beep ping")
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
