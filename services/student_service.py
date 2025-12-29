from random import randint

from numpy.random import random

from src.domain.student import Student, studentValidator
from src.repository.memory_repo import MemoryRepo
from src.repository.text_repo import StudentTextFileRepository



class StudentService:
	def __init__(self, repo):
		self._repo = repo
		self._validator = studentValidator()

	def get(self, student_id):
		return self._repo.find(student_id)

	def list_all(self):
		return self._repo.list_all()

	def add(self, student_id, student_name):
		new_student = Student(student_id, student_name)
		self._validator.validate(new_student)
		self._repo.add(new_student)

	def remove(self, student_id):

		self._repo.remove(student_id)

	def update(self, student_id, student_name):

		new_student = Student(student_id, student_name)
		self._validator.validate(new_student)
		self._repo.update(new_student)

	def search_students(self, query):

		results = []
		query_str = str(query).lower()  # Convert query to string and make it lowercase for case-insensitive matching.
		for student in self._repo.list_all():
			if query_str in str(student.id).lower() or query_str in student.name.lower():
				results.append(student)
		return results

	def generate_random(self):
		student_id=randint(1, 10000)
		student_name_list=[
    "Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah",
    "Ian", "Julia", "Kevin", "Laura", "Martin", "Natalie", "Oscar", "Paula",
    "Quentin", "Rachel", "Sam", "Tina", "Ulysses", "Valerie", "William",
    "Xandra", "Yvonne"
]
		student_name_index=randint(0, len(student_name_list) - 1)
		student_name=student_name_list[student_name_index]
		return Student(student_id, student_name)

	def generate_20(self):
		for i in range(20):
			student=self.generate_random()
			self._repo.add(student)


if __name__=="__main__":

	mem = StudentTextFileRepository("../ui/student.txt")
	service = StudentService(mem)

	service.add(101, "ANA")
	service.add(102, "MARIA")
	service.remove(103)
	service.update(102, "ALina")

	for i in service.list_all():
		print(i)

