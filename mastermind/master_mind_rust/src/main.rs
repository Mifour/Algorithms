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
use rand::{thread_rng, Rng};
#[macro_use(c)]
extern crate cute;

#[derive(Clone)]
#[derive(Debug)]
struct Code {
	code : Vec<i32>
}

fn generate_code() -> Vec<i32>{
	let mut rng = thread_rng();
	(0..5).map(|_| {
    // 0 (inclusive) to 9 (exclusive)
    	rng.gen_range(0, 9)
	}).collect()
}

impl Code {
	fn new() -> Code{
		Code{code : generate_code() }
	}

	fn score(&mut self,mut attempt : Vec<i32> ) -> (i32, i32) {
		let mut blacks = 0;
		let mut whites = 0;
		let mut to_eval : Vec<i32> = self.code.clone();
		let mut to_del = Vec::new();
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
		write!(f, "{:?}", self.code )
	}
}

fn master_mind(code = code::new()) -> i32{
	/*
	Determine the colors used. 
	While searching for colors, try to get information about positions.
	Then, try every combinaisons that match both the dots we're sure about 
	and none of the impossible combinaisons.

	Possibities of improvements:
		In phase 2, remove permutations that do not have the same score
		with the attemps than the attempts themself;
	
	Average observed score : 10.89
	Median score: 10 

	O(m colors + n! positions)
	*/
	let mut turn = 0;
	let mut completed = false;
	let mut used_colors = Vec::new();
	let mut impossible = Vec::new();
	let mut certain = vec![-1, -1, -1, -1, -1];
	let mut to_pos_test = -1;

	while not completed {
		for color in 0..9 {
			if to_pos_test != -1 {
				// use of Cute!
				let mut possible = c![i, for (i,v) in (&certain).iter().enumerate(), if v == -1];
				for to_remove in c![k, for nope in impossible for (k,v) in (&nope).iter.enumerate(), if v == to_pos_test] {
					if possible.contains(to_remove){
						possible.remove(*to_remove as usize);
					}
				}
				let mut position = possible[0];
				let attempt = Vec::new();
				for elem in 0..position{
					attempt.push(color);
				}
				attempt.push(to_pos_test);
				for elem in (position+1)..5{
					attempt.push(color);
				}

				let score = code.score(attempt);
				if score[0] + score[1] > used_colors.len() {
					let next_color = color;
				}
				else {
					let next_color = to_pos_test;
				}

				if score[1] > 0{
					for _ in 0..(score[0] + score[1]-1){
						used_colors.push(color);
					}
					let mut to_push = vec![-1,-1,-1,-1,-1];
					to_push[position] = to_pos_test;
					impossible.push(to_push);
				}
				else{
					for _ in 0..(score[0]-1){
						used_colors.push(color);
					}
					certain[position] = to_pos_test;
				}
				to_pos_test = next_color;
			}
			else {
				let attempt = vec![color,color,color,color,color];
				let score = code.score(attempt);
				for _ in 0..score[0]{
						used_colors.push(color);
					}
				if score[0] > 0{
					to_pos_test = color;
				}
			}
			if used_colors.len() == 5 {
				break;
			}
			turn += 1;

			// 2nd phase, generating possibilities, removing impossible ones
		}
	}
	return turn;

}

fn main() {
	let mut res = Vec::new();
	for _ in 0..10000{
		let code = Code::new();
		res.push(master_mind(code));
	}
	let mut mean = 0;
	for score in res.iter(){
		mean += score;
	}
	mean = mean / res.len();
	println!("average score is {:?}", mean);
}
