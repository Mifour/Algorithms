fn bubble_sort(mut array: Vec<i32>) -> Vec<i32>{
	let mut good = false;
	let mut swapped = false;
	
	while !good {
		for n in 0..array.len()-1{
			swapped = false;

			if array[n] > array[n+1]{
				let tmp = array[n];
				array[n] = array[n+1];
				array[n+1] = tmp;
				swapped = true;
				break;
			}
		}
		if !swapped {good = true;}
	}

	return array;

}


fn main() {
	let array = vec![1,0,2,6,9,4];

	println!("{:?}", bubble_sort(array));
}