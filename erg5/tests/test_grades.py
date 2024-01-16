from grades import calculate_mean, search_student, sort_students

# Defines test function for calculate_mean with an empty array as input
def test_calculate_mean_empty_array():
    students = []
    assert calculate_mean(students) == 0

# Defines test function for calculate_mean with an array with one student as input
def test_calculate_mean():
    students = [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
    ]
    assert calculate_mean(students) == (75 + 82 + 90) // 3

# Defines test function for calculate_mean with an array with multiple students as input
def test_calculate_mean_multiple_students():
    students = [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
        {"name": "Bob", "math": 88, "physics": 79, "chemistry": 95},
        {"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88},
    ]
    assert calculate_mean(students) == (75 + 82 + 90 + 88 + 79 + 95 + 92 + 85 + 88) // 9

# Defines test function for search_student with an empty array as input
def test_search_student_empty_array():
    students = []
    assert search_student("Alice", students) is None

# Defines test function for search_student with an array with one student as input
def test_search_student():
    students = [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
    ]
    assert search_student("Alice", students) == {
        "name": "Alice", "math": 75, "physics": 82, "chemistry": 90
    }

# Defines test function for search_student with an array that does not contain the student input
def test_search_student_not_found():
    students = [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
    ]
    assert search_student("Bob", students) is None

# Defines test function for sort_students with an empty array as input and math as the subject
def test_sort_students_empty_array():
    students = []
    assert sort_students(students, "math") is None

# Defines test function for sort_students with an array with multiple students as input but the
# subject is not in the array
def test_sort_students_subject_not_found():
    students = [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
        {"name": "Bob", "math": 88, "physics": 79, "chemistry": 95},
        {"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88},
    ]
    assert sort_students(students, "history") is None

# Defines test function for sort_students with an array with multiple students as input
# and math as the subject
def test_sort_students_math():
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

# Defines test function for sort_students with an array with multiple students as input
# and physics as the subject
def test_sort_students_physics():
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

# Defines test function for sort_students with an array with multiple students as input
# and chemistry as the subject
def test_sort_students_chemistry():
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
