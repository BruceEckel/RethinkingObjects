//: src/rust/inheritance/src/main.rs
struct Person;
struct Robot;

trait Base {
  fn eat(&self);
  fn speak(&self);
}

impl Base for Person {
  fn eat(&self) { println!("eating pizza"); }
  fn speak(&self) { println!("blah blah"); }
}

impl Base for Robot {
  fn eat(&self) { println!("charging"); }
  fn speak(&self) { println!("beep ping"); }
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

fn main() {
  let v: Vec<&dyn Everything> = vec![&Person{}, &Robot{}];
  for e in v.iter() {
    e.do_everything();
  }
}
