from numpy.lib._datasource import Repository

from src.domain.discipline import Discipline
from src.domain.grade import Grade
from src.domain.student import Student

class RepositoryIterator():
	def __init__(self, data):
		self.__data = data
		self.__pos = -1

	def __next__(self):
		self.__pos += 1
		if len(self.__data) == self.__pos:

			raise StopIteration()

		return self.__data[self.__pos]

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



class MemoryRepo:
	def __init__(self):
		self._data={}


	def add(self, element):


		self._data[element.id]=element

	def remove(self, id):

		return self._data.pop(id)


	def find(self, id):
		if id not in self._data:
			return None
		return self._data[id]

	def update(self, element):


		self._data[element.id]=element

	def list_all(self):
		return list(self._data.values())

	def __len__(self):
		return len(self._data)

	def __getitem__(self, key):
		if key not in self._data:
			return None
		return self._data[key]
	def __iter__(self):
		return RepositoryIterator(list(self._data.values()))




