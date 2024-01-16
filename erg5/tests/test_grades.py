import sys
sys.path.append('../erg5')

from grades import calculate_mean, search_student, sort_students

def test_calculate_mean_empty_array():
    """
    Test function for calculate_mean with an empty array as input.
    """
    students = []
    assert calculate_mean(students) == 0


def test_calculate_mean():
    """
    Test function for calculate_mean with an array with one student as input.
    """
    students = [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
    ]
    assert calculate_mean(students) == (75 + 82 + 90) // 3

def test_calculate_mean_multiple_students():
    """
    Test function for calculate_mean with an array with multiple students as input.
    """
    students = [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
        {"name": "Bob", "math": 88, "physics": 79, "chemistry": 95},
        {"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88},
    ]
    assert calculate_mean(students) == (75 + 82 + 90 + 88 + 79 + 95 + 92 + 85 + 88) // 9

def test_search_student_empty_array():
    """
    Test function for search_student with an empty array as input.
    """
    students = []
    assert search_student("Alice", students) is None

def test_search_student():
    """
    Test function for search_student with an array with one student as input.
    """
    students = [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
    ]
    assert search_student("Alice", students) == {
        "name": "Alice", "math": 75, "physics": 82, "chemistry": 90
    }

def test_search_student_multiple_students():
    """
    Test function for search_student with an array with multiple students as input
    and the student input is the first student in the array.
    """
    students = [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
        {"name": "Bob", "math": 88, "physics": 79, "chemistry": 95},
        {"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88},
    ]
    assert search_student("Alice", students) == {
        "name": "Alice", "math": 75, "physics": 82, "chemistry": 90
    }

def test_search_student_not_found():
    """
    Test function for search_student with an array that does not contain the student input.
    """
    students = [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
    ]
    assert search_student("Bob", students) is None

def test_sort_students_empty_array():
    """
    Test function for sort_students with an empty array as input and math as the subject.
    """
    students = []
    assert sort_students(students, "math") is None

def test_sort_students_subject_not_found():
    """
    Test function for sort_students with an array with multiple students as input but the
    subject is not in the array.
    """
    students = [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
        {"name": "Bob", "math": 88, "physics": 79, "chemistry": 95},
        {"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88},
    ]
    assert sort_students(students, "history") is None

def test_sort_students_math():
    """
    Test function for sort_students with an array with multiple students as input
    and math as the subject.
    """
    students = [
        {"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88},
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
        {"name": "Bob", "math": 88, "physics": 79, "chemistry": 95},
    ]
    assert sort_students(students, "math") == [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
        {"name": "Bob", "math": 88, "physics": 79, "chemistry": 95},
        {"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88},
    ]

def test_sort_students_physics():
    """
    Test function for sort_students with an array with multiple students as input
    and physics as the subject.
    """
    students = [
        {"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88},
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
        {"name": "Bob", "math": 88, "physics": 79, "chemistry": 95},
    ]
    assert sort_students(students, "physics") == [
        {"name": "Bob", "math": 88, "physics": 79, "chemistry": 95},
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
        {"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88},
    ]

def test_sort_students_chemistry():
    """
    Test function for sort_students with an array with multiple students as input
    and chemistry as the subject.
    """
    students = [
        {"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88},
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
        {"name": "Bob", "math": 88, "physics": 79, "chemistry": 95},
    ]
    assert sort_students(students, "chemistry") == [
        {"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88},
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
        {"name": "Bob", "math": 88, "physics": 79, "chemistry": 95},
    ]
