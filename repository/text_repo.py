from src.domain import student
from src.domain.discipline import Discipline
from src.domain.grade import Grade
from src.domain.student import Student

from src.repository.memory_repo import MemoryRepo, RepositoryIterator

class ValidatorException(Exception):
	def __init__(self, message):
		self._message = message

		@property
		def messages(self):
			return self._message

	def __str__(self):
			return self._message

class Validator:
	def __init__(self):
		pass

	def validate_add(self, elements_list, element):

		if elements_list:
			if any(e.id == element.id for e in elements_list):
				print(ValidatorException("Element with the same id already exists"))
				return False
		return True

	def validate_remove_update(self, elements_list, element):
		if elements_list:
			if not any(e.id == element for e in elements_list):
				print( ValidatorException("Element doesn't exist"))
				return False
		return True



class StudentTextFileRepository(MemoryRepo):
	def __init__(self, fileName):
		super().__init__()
		self.__fileName = fileName
		self.__loadFile()
		self._validator = Validator()

	def __loadFile(self):
		lines = []
		try:
			fin = open(self.__fileName, "rt")
			lines = fin.readlines()
			fin.close()
		except IOError:
			pass

		for line in lines:
			current_line = line.split(" ")
			newStudent = Student(int(current_line[0].strip()), current_line[1].strip())
			super().add(newStudent)

	def __saveFile(self):
		fout = open(self.__fileName, "wt")

		for student in self:
			studentString = str(student.id) + " " + str(student.name) + "\n"
			fout.write(studentString)

		fout.close()

	def add(self, student: Student):
		self._validator.validate_add(self.list_all(), student)
		super().add(student)
		self.__saveFile()

	def remove(self, student_id):
		self._validator.validate_remove_update(self.list_all(), student_id)
		super().remove(student_id)
		self.__saveFile()
	def update(self, student):
		self._validator.validate_remove_update(self.list_all(), student.id)
		super().update(student)
		self.__saveFile()
	def list_all(self):
		return super().list_all()

	def __len__(self):
		super().__init__()

	def __getitem__(self, key):
		super().__getitem__(key)
	def __iter__(self):
		return RepositoryIterator(list(self._data.values()))


class DisciplineTextFileRepository(MemoryRepo):
	def __init__(self, fileName):
		super().__init__()
		self.__fileName = fileName
		self.__loadFile()
		self._validator = Validator()

	def __loadFile(self):
		lines = []
		try:
			fin = open(self.__fileName, "rt")
			lines = fin.readlines()
			fin.close()
		except IOError:
			pass

		for line in lines:
			current_line = line.split(" ")
			newDiscipline = Discipline(int(current_line[0].strip()), current_line[1].strip())
			super().add(newDiscipline)

	def __saveFile(self):
		fout = open(self.__fileName, "wt")

		for discipline in self:
			disciplineString = str(discipline.id) + " " + str(discipline.name) + "\n"
			fout.write(disciplineString)

		fout.close()

	def add(self, discipline: Discipline):
		self._validator.validate_add(self.list_all(), discipline)
		super().add(discipline)
		self.__saveFile()

	def remove(self, discipline_id):
		self._validator.validate_remove_update(self.list_all(), discipline_id)
		super().remove(discipline_id)
		self.__saveFile()

	def update(self, discipline: Discipline):
		self._validator.validate_remove_update(self.list_all(), discipline.id)
		super().update(discipline)
		self.__saveFile()

	def list_all(self):
		return super().list_all()

	def __len__(self):
		super().__init__()

	def __getitem__(self, key):
		super().__getitem__(key)
	def __iter__(self):
		return RepositoryIterator(list(self._data.values()))


class GradeTextFileRepository(MemoryRepo):
	def __init__(self, fileName):
		super().__init__()
		self.__fileName = fileName
		self.__loadFile()

	def __loadFile(self):
		lines = []
		try:
			fin = open(self.__fileName, "rt")
			lines = fin.readlines()
			fin.close()
		except IOError:
			pass

		for line in lines:
			current_line = line.split(" ")
			newGrade = Grade(int(current_line[0].strip()), int(current_line[1].strip()), int(current_line[2].strip()))
			super().add(newGrade)

	def __saveFile(self):
		fout = open(self.__fileName, "wt")

		for grade in self:
			gradeString = str(grade.discipline_id) + " " + str(grade.student_id) +" " + str(grade.grade_value) + "\n"
			fout.write(gradeString)

		fout.close()

	def add(self, grade: Grade):
		super().add(grade)
		self.__saveFile()

	def remove(self, grade_id):
		super().remove(grade_id)
		self.__saveFile()

	def update(self, grade: Grade):
		super().update(grade)
		self.__saveFile()

	def list_all(self):
		return super().list_all()

	def __len__(self):
		super().__init__()

	def __getitem__(self, key):
		super().__getitem__(key)

	def __iter__(self):
		return RepositoryIterator(list(self._data.values()))






