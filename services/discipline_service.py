from random import randint

from src.domain.discipline import Discipline, disciplineValidator

from src.repository.memory_repo import MemoryRepo
from src.repository.text_repo import DisciplineTextFileRepository



class DisciplineService:
	def __init__(self, repo):
		self._repo = repo
		self._validator = disciplineValidator()

	def get(self, discipline_id):
		return self._repo.get(discipline_id)

	def list_all(self):
		return self._repo.list_all()

	def add(self, discipline_id, discipline_name):
		new_discipline = Discipline(discipline_id, discipline_name)
		self._validator.validate(new_discipline)
		self._repo.add(new_discipline)

	def remove(self, discipline_id):

		self._repo.remove(discipline_id)

	def update(self, discipline_id, discipline_name):
		new_discipline = Discipline(discipline_id, discipline_name)
		self._validator.validate(new_discipline)
		self._repo.update(new_discipline)


	def search_disciplines(self, query):

		results = []
		query_str = str(query).lower()  # Convert query to string and make it lowercase for case-insensitive matching.
		for discipline in self._repo.list_all():
			if query_str in str(discipline.id).lower() or query_str in discipline.name.lower():
				results.append(discipline)
		return results

	def generate_random(self):
		discipline_id=randint(1, 10000)
		discipline_name_list=[
    "Mathematics", "Physics", "Chemistry", "Biology", "Computer Science",
    "English Literature", "History", "Geography", "Economics", "Philosophy",
    "Political Science", "Sociology", "Psychology", "Anthropology",
    "Environmental Science", "Engineering", "Astronomy", "Statistics",
    "Art History", "Music", "Drama", "Dance", "Architecture", "Journalism",
    "Creative Writing"
]
		discipline_name_index=randint(0, len(discipline_name_list) - 1)
		discipline_name=discipline_name_list[discipline_name_index]
		return Discipline(discipline_id, discipline_name)

	def generate_20(self):
		for i in range(20):
			discipline=self.generate_random()
			self._repo.add(discipline)





