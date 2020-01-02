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
use std::collections::VecDeque;
extern crate rand;
use rand::{thread_rng, Rng};


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

fn permute(used: &mut Vec<i32>, unused: &mut VecDeque<i32>, mut vector : &mut Vec<Vec<i32>>) {
    if unused.is_empty() {
        vector.push(used.to_vec());
    } else {
        for _ in 0..unused.len() {
            used.push(unused.pop_front().unwrap());
            permute(used, unused, &mut vector);
            unused.push_back(used.pop().unwrap());
        }
    }
}

fn master_mind(mut code: Code) -> i32{
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
	//let code = Code::new();
	let mut turn = 0;
	let mut completed = false;
	let mut used_colors = Vec::new();
	let mut impossible = Vec::<Vec<i32>>::new();
	let mut certain = vec![-1, -1, -1, -1, -1];
	let mut to_pos_test = -1;
	let mut next_color = -1;

	while !completed {
		for color in 0..9 {
			if to_pos_test != -1 {
				// use of Cute!
				let mut possible = Vec::new();
				for (i,v) in certain.iter().enumerate() { 
					if *v == -1 {
						possible.push(i);
					}
				}
				let mut to_remove = Vec::new();
				for nope in impossible.iter() {
					for (k,v) in nope.iter().enumerate() {
						if *v == to_pos_test {
							to_remove.push(k);
						}
					}
				}
				for elem in to_remove {
					if possible.contains(&elem){
						possible.remove(elem as usize);
					}
				}
				let mut position = possible[0];
				let mut attempt = Vec::new();
				for elem in 0..position{
					attempt.push(color);
				}
				attempt.push(to_pos_test);
				for elem in (position+1)..5{
					attempt.push(color);
				}

				let score = code.score(attempt);
				if score.0 + score.1 > used_colors.len() as i32 {
					next_color = color;
				}
				else {
					next_color = to_pos_test;
				}

				if score.0 > 0{
					for _ in 0..(score.0 + score.1-1){
						used_colors.push(color);
					}
					let mut to_push = vec![-1,-1,-1,-1,-1];
					to_push[position] = to_pos_test;
					impossible.push(to_push);
				}
				else{
					for _ in 0..(score.0-1){
						used_colors.push(color);
					}
					certain[position] = to_pos_test;
				}
				to_pos_test = next_color;
			}
			else {
				let attempt = vec![color,color,color,color,color];
				let score = code.score(attempt);
				for _ in 0..score.0{
						used_colors.push(color);
					}
				if score.0 > 0{
					to_pos_test = color;
				}
			}
			if used_colors.len() == 5 {
				break;
			}
			turn += 1;

			// 2nd phase, generating possibilities, removing impossible ones
		    let mut queue : VecDeque<i32> = VecDeque::from(used_colors);
		    let mut permutations = Vec::<Vec<i32>>::new();
		    permute(&mut Vec::new(), &mut queue, &mut permutations);
		    for attempt in permutations.iter() {
		    	let mut tmp = Vec::new();
		    	for index in 0..5{
		    		if certain[index] == -1 {
		    			tmp.push(attempt[index]);
		    		}
		    		else {
		    			tmp.push(certain[index]);
		    		}
		    	}
		    	let mut possible : bool = true;
		    	for nope in impossible.iter(){
		    		for index in 0..5{
		    			if nope[index] == attempt[index] {
		    				possible = false;
		    			}
		    		}
		    	}

		    	if *attempt == tmp && possible {
		    		let score = code.score(attempt.to_vec());
		    		completed = score == (5,0);
		    		if completed {
		    			break;
		    		}
		    		turn +=1;
		    	}
		    	
		    }
		}
	}
	return turn;

}

fn main() {
	let mut res = Vec::new();
	for _ in 0..10000{
		let mut code = Code::new();
		res.push(master_mind(code));
	}
	let mut mean = 0;
	for score in res.iter(){
		mean += score;
	}
	mean = mean / (res.len() as i32);
	println!("average score is {:?}", mean);
}
