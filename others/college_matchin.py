from collections import deque

class Student:
	def __init__(self, id, order=[], college=None):
		self.id = id
		self.order = order
		self.mask = []
		self.college = college

class College:
	def __init__(self, id, order={}, max_size=0, current_size=0, worst=0, students=[]):
		self.id = id
		self.order = order
		self.max_size = max_size
		self.current_size = current_size
		self.worst = worst
		self.students = students
	def update_worst(self):
		self.worst = max([self.order[student] for student in self.students])

def Gale_Shapley(students, colleges):
	"""
		Implementation of Gale-Shapley algorithm
		See https://en.wikipedia.org/wiki/Gale–Shapley_algorithm

		It make sure that each couple student-college is fair and the matching is stable.
		If the student ask for college, the solution is the best stable solution for students.
	"""

	# first run
	tmp = deque()
	done = False

	first_wishes = {}
	for student in students:
		first_wishes[colleges[student.order[0]].id] = (
			first_wishes[colleges[student.order[0]].id].append(student.id) 
			if colleges[student.order[0]] in first_wishes
			else [student.id]
		)

	first_acceptance = {}
	for college in colleges.values():
		if college.id in first_wishes:
			best_candidate = min([college.order[candidate] for candidate in first_wishes[college.id]])
			accepted = [k for k,v in college.order.items() if v == best_candidate ][0]
			first_acceptance[accepted] = college.id

	for student in students:
		if student.id in first_acceptance.keys():
			college = colleges[first_acceptance[student.id]]
			college.current_size+=1
			student.college = college
			college.students.append(student.id)
			college.update_worst()
		else:
			tmp.append(student)
			student.mask.append(0)

	# 2nd run
	while tmp and not done:
		student = tmp.popleft()
		id = student.id
		college = colleges[student.order[len(student.mask)]]

		if college.current_size < college.max_size:
			college.current_size+=1
			college.worst = max(college.worst, college.order[id])
			student.college = college
		else:
			if college.order[id] < college.worst:
				key = [k for k,v in college.order.items() if v == college.worst][0]
				rejected = students[key]
				rejected.college = None
				college.students.remove(rejected.id)
				tmp.append(rejected)

				student.college = college
				college.students.append(id)
				college.update_worst()

			else:
				student.mask.append(0)
				tmp.append(student)
		tmp_copy = list(tmp.copy())
		done = all([len(student.mask) >= len(student.order) for student in tmp_copy])


colleges = {
	0:College(id=0, order={0:0, 1:2, 2:1}, max_size=1, current_size=0, worst=0, students=[]),
	1:College(id=1, order={0:1, 1:0, 2:2}, max_size=1, current_size=0, worst=0, students=[]),
	2:College(id=2, order={0:1, 1:2, 2:0}, max_size=1, current_size=0, worst=0, students=[])
}

alix = Student(id=0, order=[1,0,2], college=None)
bob = Student(id=1, order=[0,1,2], college=None)
charlie = Student(id=2, order=[0,1,2], college=None)
students = [alix, bob, charlie]

Gale_Shapley(students, colleges)

print("------ resutls ------")
for student in students:
	print(f"student {student.id} is accepted at {student.college.id}")
	# should end with 0:0, 1:1, 2:2
	