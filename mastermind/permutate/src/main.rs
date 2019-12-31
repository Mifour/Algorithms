extern crate permutate;
use permutate::Permutator;
use std::io::{self, Write};

fn main() {
    let stdout = io::stdout();
    let mut stdout = stdout.lock();
    let list: Vec<i32> = vec![0,1,2,3,4];

    // Pass the `Vec<&[&str]>` as an `&[&[&str]]`
    let mut permutator = Permutator::new(list);

    if let Some(mut permutation) = permutator.next() {
        for element in &permutation {
            let _ = stdout.write(element.as_bytes());
        }
        stdout.write(b"\n");
        
    }
}