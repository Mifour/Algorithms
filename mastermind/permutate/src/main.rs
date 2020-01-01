
use std::collections::VecDeque;
 
fn permute_action<T, F: Fn(&[T])>(used: &mut Vec<T>, unused: &mut VecDeque<T>, action: &F) {
    if unused.is_empty() {
        action(used);
    } else {
        for _ in 0..unused.len() {
            used.push(unused.pop_front().unwrap());
            permute_action(used, unused, action);
            unused.push_back(used.pop().unwrap());
        }
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
 
fn main() {
    let mut queue = (1..4).collect::<VecDeque<_>>();
    permute_action(&mut Vec::new(), &mut queue, &|perm| println!("{:?}", perm));

    let vector = vec![0,1,2,3,4];
    let mut other_queue : VecDeque<i32> = VecDeque::from(vector);
    let mut permutation = Vec::<Vec<i32>>::new();
    permute(&mut Vec::new(), &mut other_queue, &mut permutation);
    println!("number of permutations{:?}", permutation.len() );
    for perm in permutation.iter() {
        if perm[1] != 2{
            println!("{:?}", perm);
        }
    }
}