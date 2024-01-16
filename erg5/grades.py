# Defines a function that calculates the mean of an array of grades
def calculate_mean(arr):
    total_sum = 0
    count = 0
    for student in arr:
        for subject, grade in student.items():
            if subject != "name":  # Exclude the 'name' field
                total_sum += grade
                count += 1
    grades_mean = total_sum // count if count else 0
    return grades_mean

# Defines a function that searches for a student by name
def search_student(name, arr):
    for student in arr:
        if student["name"] == name:
            return student
        return None

# Defines a function that sorts an array of students by a subject
def sort_students(arr, subject):
    for student in arr:
        if subject not in student:
            return None
        arr.sort(key=lambda x: x[subject])
        return arr

# Defines the main function
def main():
    grades = [
        {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
        {"name": "Bob", "math": 88, "physics": 79, "chemistry": 95},
        {"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88},
    ]
    print(calculate_mean(grades))
    print(search_student("Bob", grades))
    print(sort_students(grades, "math"))
