import unittest

from src.repository.memory_repo import MemoryRepo
from src.services.student_service import StudentService

class TestStudentService(unittest.TestCase):
    def setUp(self):
        # Set up an in-memory repository for testing
        self.repo = MemoryRepo()
        self.service = StudentService(self.repo)

    def test_add_student(self):
        # Test adding a student
        self.service.add(1, "John Doe")
        student = self.service.get(1)
        self.assertIsNotNone(student)
        self.assertEqual(student.id, 1)
        self.assertEqual(student.name, "John Doe")

    def test_remove_student(self):
        # Add and then remove a student
        self.service.add(2, "Jane Doe")
        self.service.remove(2)
        student = self.service.get(2)
        self.assertIsNone(student)

    def test_update_student(self):
        # Add and then update a student
        self.service.add(3, "Mike Smith")
        self.service.update(3, "Michael Smith")
        student = self.service.get(3)
        self.assertIsNotNone(student)
        self.assertEqual(student.name, "Michael Smith")

    def test_list_all(self):
        # Test listing all students
        self.service.add(4, "Alice Johnson")
        self.service.add(5, "Bob Brown")
        students = self.service.list_all()
        self.assertEqual(len(students), 2)

    def test_search_students(self):
        # Test searching for students
        self.service.add(6, "Chris Martin")
        self.service.add(7, "Christine Brown")
        results = self.service.search_students("Chris")
        self.assertEqual(len(results), 2)
        results = self.service.search_students("Martin")
        self.assertEqual(len(results), 1)



if __name__ == "__main__":
    unittest.main()