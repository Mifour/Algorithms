/*
Super MasterMind game and solver in Rust!
by Thomas Dufour, 30/12/2019

rules: 
	the code is 5 digits from 0 to 9 (8 colors + None color)
	number of unique codes = 59049
	the score is :
		1 black for 1 color well placed
		1 white for 1 color misplaced
		there are no information about position
	the game ends when all 5 dots are guessed (score = 5 blacks, 0 whites)
*/
use std::fmt::{self, Formatter, Display};
extern crate rand;
use rand::thread_rng;

#[derive(Clone)]
#[derive(Debug)]
struct Code {
	code : Vec<i32>
}

fn generate_code() -> Vec<i32>{
	(0..5).map(|_| {
	    // 0 (inclusive) to 9 (exclusive)
	    rand::thread_rng().gen_range(0, 9)
	}).collect()
}

impl Code {
	fn new() -> Code{
		Code{code : generate_code() }
	}

	fn score(&mut self, attempt : Vec<i32> ) -> (i32, i32) {
		let mut blacks = 0;
		let mut whites = 0;
		let mut to_eval : Vec<i32> = self.code.clone();
		let mut to_del : Vec<i32>;
		let mut deleted = 0_i32;

		for dot in 0..5{
			if attempt[dot] == to_eval[dot]{
				blacks +=1 ;
				to_del.push(dot as i32);
			}
		}
		
		for dot in to_del.iter(){
			to_eval.remove((*dot as i32 -deleted) as usize);
			attempt.remove((*dot as i32 -deleted) as usize);
			deleted +=1
		}
			

		for dot in attempt.iter(){
			if to_eval.contains(dot){
				whites +=1;
				to_eval.remove(*dot as usize);
			}
		}

		return (blacks, whites)
	}
}

impl Display for Code {
	fn fmt(&self, f: &mut Formatter) -> fmt::Result {
		write!(f, "{:?}, ", self.code )
	}
}

fn main() {
	let code = Code::new();
	println!("{:?}", code);
}
