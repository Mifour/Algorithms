fn fibonacci(n:i32) -> i32 {
	if n == 0 {return 0}
	if n == 1 {return 1}
	else{
		return fibonacci(n-1) + fibonacci(n-2)
	}
}


fn main() {
	println!("{:?}", fibonacci(0));
	println!("{:?}", fibonacci(1));
	println!("{:?}", fibonacci(2));
	println!("{:?}", fibonacci(8));
}