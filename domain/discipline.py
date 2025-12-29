class ValidatorException(Exception):
	def __init__(self, message):
		self._message = message

		@property
		def messages(self):
			return self._message

	def __str__(self):
			return self._message

class disciplineValidator:
	def __init__(self):
		pass

	def validate(self, element):
		if not type(element.id) == int or element.id <= 0:
			print(ValidatorException("Id not valid"))
		if (not type(element.name) == str) or len(element.name.strip()) == 0:
			print(ValidatorException("Name not valid"))

class Discipline:

	def __init__(self, discipline_id, discipline_name: str):
		self.__id = discipline_id
		self.__name = discipline_name

	@property
	def id(self):
		return self.__id
	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, new_name):
		self.__name = new_name

	def __str__(self):
		return str(self.__id) + " " + self.__name



