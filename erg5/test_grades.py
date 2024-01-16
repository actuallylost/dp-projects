from grades import calculate_mean, search_student, sort_students

# Defines test function for calculate_mean with an empty array as input
def test_calculate_mean_empty_array():
    grades = []
    assert calculate_mean(grades) == 0

# Defines test function for calculate_mean with an array with one student as input
def test_calculate_mean():
    grades = [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
    ]
    assert calculate_mean(grades) == (75 + 82 + 90) // 3

# Defines test function for calculate_mean with an array with multiple students as input
def test_calculate_mean_multiple_students():
    grades = [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
        {"name": "Bob", "math": 88, "physics": 79, "chemistry": 95},
        {"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88},
    ]
    assert calculate_mean(grades) == (75 + 82 + 90 + 88 + 79 + 95 + 92 + 85 + 88) // 9

# Defines test function for search_student with an empty array as input
def test_search_student_empty_array():
    grades = []
    assert search_student("Alice", grades) is None

# Defines test function for search_student with an array with one student as input
def test_search_student():
    grades = [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
    ]
    assert search_student("Alice", grades) == {
        "name": "Alice", "math": 75, "physics": 82, "chemistry": 90
    }

# Defines test function for search_student with an array that does not contain the student input
def test_search_student_not_found():
    grades = [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
    ]
    assert search_student("Bob", grades) is None

def test_sort_students_empty_array():
    grades = []
    assert sort_students(grades, "math") is None
