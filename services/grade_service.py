from src.domain.grade import Grade, gradeValidator
from src.repository.memory_repo import MemoryRepo
from src.repository.text_repo import StudentTextFileRepository, GradeTextFileRepository, DisciplineTextFileRepository

from src.services.student_service import StudentService


class GradeService:
	def __init__(self, repo, stud_repo, dis_repo):
		self._repo = repo
		self._stud_repo = stud_repo
		self._dis_repo = dis_repo
		self._validator = gradeValidator()

	def get_all(self):
		return self._repo.get_all()

	def add(self, discipline_id, student_id, grade_value:int ):

		new_grade = Grade(discipline_id, student_id, grade_value)
		self._validator.validate_add_grade(self._stud_repo.list_all(),self._dis_repo.list_all(), new_grade)
		new_grade.id = len(self._repo.list_all()) + 1
		self._repo.add(new_grade)

	def list_all(self):
		return self._repo.list_all()

	def list_all_students(self):
		return self._stud_repo.list_all()
	def list_all_disciplines(self):
		return self._dis_repo.list_all()

	def remove_grade_student(self,  student_id):

		for grade in self._repo.list_all():
			if grade.student_id == student_id:
				self._repo.remove(grade.id)

	def remove_grade_discipline(self,  discipline_id):

		for grade in self._repo.list_all():
			if grade.discipline_id == discipline_id:
				self._repo.remove(grade.id)



if __name__=="__main__":

	std = StudentTextFileRepository("../ui/student.txt")
	grd = GradeTextFileRepository("../ui/grade.txt")
	dis = DisciplineTextFileRepository("../ui/discipline.txt")

	service = GradeService(grd, std, dis)


	service.add(1, 10, 10)
	service.add(1, 11, 10)
	service.add(1, 12, 10)
	service.add(1, 13, 10)
	service.add(2, 3, 4 )
	service.add(3, 3, 4)
	service.add(4, 3, 4)


	service.remove_grade_student(3)
	for i in service.list_all():
		print(i)