def calculate_mean(arr):
    """
    Calculate the mean of an array of grades.
    @param arr - The array of grades.
    """
    total_sum = 0
    count = 0
    for student in arr:
        for subject, grade in student.items():
            if subject != "name":  # Exclude the 'name' field
                total_sum += grade
                count += 1
    grades_mean = total_sum // count if count else 0
    return grades_mean

def search_student(name, arr):
    """
    Search for a student by name.
    @param name - The name of the student to search for.
    @param arr - The array of students.
    """
    for student in arr:
        if student["name"] == name:
            return student
        return None

def sort_students(arr, subject):
    """
    Sort an array of students by a subject.
    @param arr - The array of students.
    @param subject - The subject to sort by.
    """
    for student in arr:
        if subject not in student:
            return None
        arr.sort(key=lambda x: x[subject])
        return arr

def main():
    """
    The main function.
    """
    students = [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
        {"name": "Bob", "math": 88, "physics": 79, "chemistry": 95},
        {"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88},
    ]
    print(calculate_mean(students))
    print(search_student("Bob", students))
    print(sort_students(students, "math"))
