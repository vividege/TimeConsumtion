import unittest
from unittest.mock import Mock, patch

from PythonUnitTest.domain.student import Student
from PythonUnitTest.service import student_service

class TestStudentService(unittest.TestCase):

    def test_change_name_with_record(self):
        # 准备工作
        student_service.find_student_by_id = Mock()# 并不想运行find_student_by_id这个方法，而是使用一个模拟的find_student_by_id()
        # student_service.find_student_by_id.return_value = Student(1, 'Tom')
        student = Mock(id=1, name='Tom') # 模拟了Student这个类，
        student_service.find_student_by_id.return_value = student

        student_service.save_student = Mock()

        # Action
        student_service.change_name(1, "Jack")

        # Assert
        student_service.save_student.assert_called()
        self.assertEqual("Jack", student.name)

    def test_change_name_without_record(self):
        # 准备工作
        student_service.find_student_by_id = Mock()# 并不想运行find_student_by_id这个方法，而是使用一个模拟的find_student_by_id()
        # student_service.find_student_by_id.return_value = Student(1, 'Tom')
        student = Mock(id=1, name='Tom') # 模拟了Student这个类，
        student_service.find_student_by_id.return_value = None

        student_service.save_student = Mock()

        # Action
        student_service.change_name(1, "Jack")

        # Assert
        # 判断该函数没有进行名字修改
        student_service.save_student.assert_not_called()

class TestStudentServiceWithPatch(unittest.TestCase):

    @patch("PythonUnitTest.service.student_service.save_student")
    @patch("PythonUnitTest.service.student_service.find_student_by_id")
    def test_change_name_with_decorator(self, find_student_mock, save_student_mock):
        # find_student_mock 和装饰器中的find_student_by_id是对应关系, 返回值有两种形式
        # 多个mock，请注意参数顺序

        # Setup
        student = Mock(id=1, name='Jack')
        find_student_mock.return_value = student

        # Action
        student_service.change_name(1, 'Tom')

        # Assert
        self.assertEqual('Tom', student.name)

    @patch("PythonUnitTest.service.student_service.save_student")
    @patch("PythonUnitTest.service.student_service.find_student_by_id")
    def test_change_name_None_with_decorator(self, find_student_mock, save_student_mock):
        # find_student_mock 和装饰器中的find_student_by_id是对应关系, 返回值有两种形式
        # 多个mock，请注意参数顺序

        # Setup
        find_student_mock.return_value = None

        # Action
        student_service.change_name(1, 'Tom')

        # Assert
        save_student_mock.assert_not_called()

    @patch("PythonUnitTest.service.student_service.find_student_by_id")
    def test_change_name_with_contextmanager(self, find_student_mock):

        # Setup
        student = Mock(id=1, name='Jack')
        find_student_mock.return_value = student

        with patch("PythonUnitTest.service.student_service.save_student"):
            # Action
            student_service.change_name(1, 'Tom')

            # Assert
            self.assertEqual('Tom', student.name)