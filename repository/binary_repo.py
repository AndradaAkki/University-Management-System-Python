import pickle
from src.domain.student import Student
from src.domain.discipline import Discipline
from src.domain.grade import Grade
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
                raise ValidatorException("Element with the same ID already exists")
        return True

    def validate_remove_update(self, elements_list, element_id):
        if elements_list:
            if not any(e.id == element_id for e in elements_list):
                raise ValidatorException("Element doesn't exist")
        return True


class StudentBinaryFileRepository(MemoryRepo):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self._validator = Validator()
        self.__loadFile()

    def __loadFile(self):
        try:
            with open(self.__fileName, "rb") as file:
                self._data = pickle.load(file)
        except (IOError, EOFError):
            self._data = {}

    def __saveFile(self):
        with open(self.__fileName, "wb") as file:
            pickle.dump(self._data, file)

    def add(self, student: Student):
        self._validator.validate_add(self.list_all(), student)
        super().add(student)
        self.__saveFile()

    def remove(self, student_id):
        self._validator.validate_remove_update(self.list_all(), student_id)
        super().remove(student_id)
        self.__saveFile()

    def update(self, student: Student):
        self._validator.validate_remove_update(self.list_all(), student.id)
        super().update(student)
        self.__saveFile()

    def list_all(self):
        return super().list_all()


class DisciplineBinaryFileRepository(MemoryRepo):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self._validator = Validator()
        self.__loadFile()

    def __loadFile(self):
        try:
            with open(self.__fileName, "rb") as file:
                self._data = pickle.load(file)
        except (IOError, EOFError):
            self._data = {}

    def __saveFile(self):
        with open(self.__fileName, "wb") as file:
            pickle.dump(self._data, file)

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


class GradeBinaryFileRepository(MemoryRepo):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__loadFile()

    def __loadFile(self):
        try:
            with open(self.__fileName, "rb") as file:
                self._data = pickle.load(file)
        except (IOError, EOFError):
            self._data = {}

    def __saveFile(self):
        with open(self.__fileName, "wb") as file:
            pickle.dump(self._data, file)

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
