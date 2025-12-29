from src.domain.student import ValidatorException
from src.repository.binary_repo import StudentBinaryFileRepository, DisciplineBinaryFileRepository, \
	GradeBinaryFileRepository
from src.repository.memory_repo import MemoryRepo
from src.repository.text_repo import StudentTextFileRepository, DisciplineTextFileRepository, GradeTextFileRepository
from src.services import  grade_service
from src.services.discipline_service import DisciplineService
from src.services.grade_service import GradeService

from src.services.student_service import StudentService


class UI:
	def __init__(self, student_service, discipline_service, grade_services):
		self.__student_service = student_service
		self.__discipline_service = discipline_service
		self.__grade_service = grade_services
		self.commands = {
			"1": self.add_student,
			"2": self.add_discipline,
			"3": self.add_grade,
			"4": self.list_students,
			"5": self.list_disciplines,
			"6": self.list_grades,
			"7": self.remove_student,
			"8": self.remove_discipline,
			"9": self.update_student,
			"10": self.update_discipline,
			"11":self.search_student,
			"12":self.search_discipline,
			"0": self.exit_program
		}

	def print_menu(self):
		print("1. Add Student")
		print("2. Add Discipline")
		print("3. Add Grade")
		print("4. List Students")
		print("5. List Disciplines")
		print("6. List Grades")
		print("7. Remove Student")
		print("8. Remove Discipline")
		print("9. Update Student")
		print("10. Update Discipline")
		print("11. Search Student")
		print("12. Search Discipline")
		print("0. Exit")

	def run(self):
		self.__student_service.generate_20()
		self.__discipline_service.generate_20()
		while True:
			self.print_menu()
			command = input("Enter your choice: ")
			action = self.commands.get(command)
			if action:
				try:
					action()
				except Exception as e:
					print(f"Error: {e}")
			else:
				print("Invalid choice!")

	def add_student(self):

		try:
			student_id = int(input("Enter Student ID: "))
			name = input("Enter Student Name: ")
			self.__student_service.add( student_id, name)
			print("Student added successfully!")
		except ValidatorException as e:
			print(f"Error: {e}")
	def add_discipline(self):
		try:
			discipline_id = int(input("Enter Discipline ID: "))
			name = input("Enter Discipline Name: ")
			self.__discipline_service.add(discipline_id, name)
			print("Discipline added successfully!")
		except ValidatorException as e:
			print(f"Error: {e}")
	def add_grade(self):
		try:
			discipline_id = int(input("Enter Discipline ID: "))
			student_id = int(input("Enter Student ID: "))
			grade_value = int(input("Enter Grade Value: "))
			self.__grade_service.add(discipline_id, student_id, grade_value)
			print("Grade added successfully!")
		except ValidatorException as e:
			print(f"Error: {e}")

	def list_students(self):
		students = self.__student_service.list_all()
		if not students:
			print("No students found.")
		for student in students:
			print(student)

	def list_disciplines(self):
		disciplines = self.__discipline_service.list_all()
		if not disciplines:
			print("No disciplines found.")
		for discipline in disciplines:
			print(discipline)

	def list_grades(self):

		grades = self.__grade_service.list_all()
		if not grades:
			print("No grades found.")
		for grade in grades:
			print(grade)

	def remove_student(self):
		try:
			student_id = int(input("Enter Student ID to remove: "))
			self.__student_service.remove(student_id)
			self.__grade_service.remove_grade_student(student_id)
			print("Student removed successfully!")
		except ValidatorException as e:
			print(f"Error: {e}")
	def remove_discipline(self):
		try:
			discipline_id = input("Enter Discipline ID to remove: ")
			self.__discipline_service.remove(discipline_id)
			self.__grade_service.remove_grade_discipline(discipline_id)
			print("Discipline removed successfully!")
		except ValidatorException as e:
			print(f"Error: {e}")
	def update_student(self):
		try:
			student_id =int( input("Enter Student ID to update: "))
			new_name = input("Enter new name for Student: ")
			self.__student_service.update(student_id, new_name)
			print("Student updated successfully!")
		except ValidatorException as e:
			print(f"Error: {e}")
	def update_discipline(self):
		try:
			discipline_id = input("Enter Discipline ID to update: ")
			new_name = input("Enter new name for Discipline: ")
			self.__discipline_service.update(discipline_id, new_name)
			print("Discipline updated successfully!")
		except ValidatorException as e:
			print(f"Error: {e}")

	def search_student(self):
		query = input("Enter Student ID or Name to Search: ")
		results = self.__student_service.search_students(query)
		if results:
			print("Search Results:")
			for student in results:
				print(student)
		else:
			print("No matching students found.")
	def search_discipline(self):
		query = input("Enter Discipline ID or Name to Search: ")
		results = self.__discipline_service.search_disciplines(query)
		if results:
			print("Search Results:")
			for discipline in results:
				print(discipline)
		else:
			print("No matching disciplines found.")

	def exit_program(self):
		print("Exiting the program.")
		exit()

if __name__=="__main__":
	#stud_txt=StudentTextFileRepository("student.txt")
	#disc_txt=DisciplineTextFileRepository("discipline.txt")
	#grade_txt=GradeTextFileRepository("grade.txt")
	stud_txt=StudentBinaryFileRepository("student.pickle")
	disc_txt=DisciplineBinaryFileRepository("discipline.pickle")
	grade_txt=GradeBinaryFileRepository("grade.pickle")

	s_service= StudentService(stud_txt)
	d_service= DisciplineService(disc_txt)
	g_service= GradeService(grade_txt, s_service, d_service)
	ui = UI(s_service, d_service, g_service)
	ui.run()