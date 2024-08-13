from PythonUnitTest.domain.student import Student


def find_student_by_id(id: int) -> Student:
    # query database
    return Student(id, "Tom") # this is a fake result

def save_student(student: Student):
    # save student to database
    pass

def change_name(student_id: int, name: str):
    student = find_student_by_id(student_id)

    if student is not None:
        student.name = name
        save_student(student)
