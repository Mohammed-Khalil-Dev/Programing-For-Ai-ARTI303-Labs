"""Student record utilities for ARTI 303."""


class Student:
    """A single student record."""

    def __init__(self, name: str, age: int, gpa: float, is_enrolled: bool=True):
        if not 0.0 <= gpa <= 4.0:
            raise ValueError("GPA must be between 0 and 4.0.")
        self.name = name
        self.age = age
        self.gpa = gpa
        self.is_enrolled = is_enrolled

    def is_dean_list(self) -> bool:
        """Return True if this student's GPA qualifies for the Dean's list."""
        return self.gpa >= 3.5

    def report_line(self) -> str:
        """Return a one-line, human-readable summary of this student."""
        status = "made the Dean's list" if self.is_dean_list() else "did not make the Dean's list"
        enrollment = "is enrolled" if self.is_enrolled else "is not enrolled"
        return f"{self.name} (age {self.age}, GPA {self.gpa:.2f}) {enrollment} and {status}."

    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, age={self.age}, gpa={self.gpa})"


def average_gpa(students: list[Student]) -> float:
    total_gpa:float| int = 0
    for student in students:
        total_gpa += student.gpa

    return total_gpa / len(students) if len(students) > 0 else 0

def dean_list_students(students: list[Student]) -> list[Student]:
    dean_students: list[Student] = [student for student in students if student.is_dean_list()]
    return dean_students

def letter_grade(gpa: float | int) -> str:
    if gpa >= 3.7: return "A"
    elif gpa >= 2.7: return "B"
    elif gpa >= 1.7: return "C"
    elif gpa >= 1.0: return "D"
    else: return "F"

def oldest_student(students: list[Student]) -> Student:
    if len(students) == 0: raise ValueError("Students must have at least one student.")
    oldest = students[0]
    for student in students:
        if student.age > oldest.age:
            oldest = student

    return oldest

def group_by_enrollment(students: list[Student]) -> tuple[list[Student], list[Student]]:
    if len(students) == 0: raise ValueError("Students must have at least one student.")
    """Group students by enrollment.
    @return tuple[list[enrolled_students], list[not_enrolled_students]]"""
    enrolled_students: list[Student] = [student for student in students if student.is_enrolled]
    not_enrolled_students: list[Student] = [student for student in students if not student.is_enrolled]
    return enrolled_students, not_enrolled_students












