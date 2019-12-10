fn main() {


	let string = "abcdefghijklmnopqrstuvwxyz";
	let key: i32 = 15;

	let mut res: Vec<char> = vec![];

	for letter in string.chars() {
		res.push(
			 unsafe { std::char::from_u32_unchecked(((letter as i32 -97 + key)%26 + 97) as u32) }
		);
	}
	println!("{}",res.iter().cloned().collect::<String>());
}