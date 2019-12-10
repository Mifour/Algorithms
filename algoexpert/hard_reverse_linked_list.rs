use std::collections::LinkedList;
use std::fmt::{self, Formatter, Display};

#[derive(Clone)]
struct linked_list {
	value: u32,
	next: linked_list
}

impl linked_list {
	fn get_next(&mut self){
		return self.next;
	}
	fn set_next(&mut self, elem: linked_list){
		self.next = elem;
	}
}

impl Display for linked_list {
	fn fmt(&self, f: &mut Formatter) -> fmt::Result {
		let mut elem = self.value;
		write!(f, "{:?}, ", elem );
		elem = self.get_next();
		while self.value != NULL {
			write!(f, "{:?}, ", elem.value );
			elem = elem.get_next();
		}
	}
}

fn reverse_linked_list(mut list: linked_list) -> linked_list{
	let mut p1 = linked_list{value: NULL, next:NULL};
	let mut p2 = list.clone();

	while p2.value != NULL{
		let p3 = p2.get_next();
		p2.set_next(p1);
		p1 = p2;
		p2 = p3;
	}
}



fn reverse_LinkedList(mut list: LinkedList<u32>) -> LinkedList<u32>{
	let mut res: LinkedList<u32> = LinkedList::new();

	for elem in list.iter(){
		res.push_front(*elem);
	}

	return res;

}


fn main() {
	let mut list: LinkedList<u32> = LinkedList::new();
	list.push_back(0);
	list.push_back(2);
	list.push_back(3);
	list.push_back(4);
	list.push_back(5);

	println!("{:?}", reverse_LinkedList(list));


	list = linked_list{value:0};
	list.set_next(linked_list{value:1});
	list.get_next.set_next(linked_list{value:2});


}