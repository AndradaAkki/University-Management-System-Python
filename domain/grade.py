class ValidatorException(Exception):
	def __init__(self, message):
		self._message = message

		@property
		def messages(self):
			return self._message

	def __str__(self):
			return self._message

class gradeValidator:
	def __init__(self):
		pass

	def validate(self, element, list1):
		if not type(element.student_id) == int or element.id <= 0:
			print(ValidatorException("Student Id not valid"))
		if not type(element.student_id) == int or element.id <= 0:
			print(ValidatorException("Discipline Id not valid"))
		if (not type(element.name) == str) or len(element.name.strip()) == 0:
			print(ValidatorException("Name not valid"))

	def validate_add_grade(self, list1, list2, element):

		if int(element.grade_value) >10 or int(element.grade_value) <0 :
			print(ValidatorException("Grade must be between 0 and 10"))

		if not any(e.id == element.student_id for e in list1):
			print(ValidatorException("Student not registered"))
			return False
		if not any(e.id == element.discipline_id for e in list2):
			print(ValidatorException("Discipline not registered"))
			return False
		return True

class Grade:
	def __init__(self,  discipline_id, student_id, grade_value):
		self.__id = 0
		self.__discipline_id = discipline_id
		self.__student_id = student_id
		self.__grade_value = grade_value
	@property
	def id(self):
		return self.__id
	@id.setter
	def id(self, id):
		self.__id = id
	@property
	def discipline_id(self):
		return self.__discipline_id
	@property
	def student_id(self):
		return self.__student_id
	@property
	def grade_value(self):
		return self.__grade_value

	def __str__(self):
		return str(self.__discipline_id) + " " + str(self.__student_id) + " " + str(self.__grade_value)



