# README

## Introduction

This file will detail the implementation and testing for `binary_search.py` and `grades.py` files.

## Testing

Using the library `PyTest` I tested the code to make sure it works as intended.

## Binary Search

### Description

This is a simple implementation of binary search algorithm in Python.

### Original code snippet

```python
def binarySearch( A, key ):
last = len( A ) - 1
first = 0
pos = -1
while first <= last and pos == -1 :
mid = (last + first) // 2
if A[ mid ]==key :
pos = mid
elif A[ mid ] < key :
first = mid + 1
else:
last = mid - 1
return pos

A = [23, 51, 5, 15, 7]
```

### Fixed code snippet

```python
def binary_search(arr, key):
    arr.sort()
    print(arr)
    last = len(arr) - 1
    first = 0
    pos = -1
    while first <= last and pos == -1:
        mid = (last + first) // 2
        if arr[mid] == key:
            pos = mid
        elif arr[mid] < key:
            first = mid + 1
        else:
            last = mid - 1
    return pos

def main():
    arr = [23, 51, 5, 15, 7]
    print(binary_search(arr, 23))
```

The fixed code snippet implemented the following changes

- Changed the function name to account for Python's naming conventions.
- Changed the indentation of the code in order for it to be runnable.
- Sorted the array before starting the search, since binary search cannot be performed on an unsorted array.
- Added a main function to call the binary_search function.

### Final code snippet

```python
def binary_search(arr, key):
    """
    Implement binary search.
    @param arr - The array to search.
    @param key - The key to search for.
    """
    # Defines the first and last index of the array
    last = len(arr) - 1
    first = 0
    pos = -1
    # Loops through the array until the key is found or the first index is greater than the last
    while first <= last and pos == -1:
        mid = (last + first) // 2
        if arr[mid] == key:
            pos = mid
        elif arr[mid] < key:
            first = mid + 1
        else:
            last = mid - 1
    return pos

def main():
    """
    The main function.
    """
    arr = [23, 51, 5, 15, 7]
    arr.sort()
    print(binary_search(arr, 23))
```

The final code snippet adds comments to the code to make it more readable and understandable. It also assumes that the array is sorted before calling the function.

### Tests

The test cases for the binary search algorithm are the following:

- Empty array as input, which expect the output to be `-1`.
- Array with one element as input and the key element being present in the array, which expect the output to be `0`.
- Sorted array with five elements and the key element being present in the array, which expects the output to be `2`.
- Sorted array with five elements and the key element not being present in the array, which expects the output to be `-1`.

## Grades

### Input

The input array for any of the three functions should have the following format:

```python
students = [
    {
        "name": "John",
        "math": 90,
        "physics": 80,
        "chemistry": 85,
    }
]
```

### Description

This file contains the implementation of three functions:

- `calculate_mean` - Which takes in an array of students and returns the mean of all subject elements in the array.
- `search_student` - Which takes in an array of students and a student name and returns the entry of the student in the array, if it exists.
- `sort_students` - Which takes in an array of students and a subject key, sorts it by ascending order of the subject and returns the sorted array.

### Final code snippet

```python
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
```

The final code snippet implements all three functions along with comments to make it more readable and understandable. It also adds a main function to call the three functions.

### Tests

The test cases for the grades functions are the following:

`calculate_mean`

- Empty array as input, which expects the output to be `0`.
- Array with one student as input, which expects the output to be `82`.
- Array with three students as input, which expects the output to be `86`.

`search_student`

- Empty array and `"Alice"` as input, which expects the output to be `None`.
- Array with one student and `"Alice"` as input, which expects the output to be `{"name": "Alice", "math": 75, "physics": 82, "chemistry": 90}`.
- Array with three students and `"Alice"` as input, which expects the output to be `{"name": "Alice", "math": 75, "physics": 82, "chemistry": 90}`.
- Array with one student and a different one's name (`"Bob"`) as input, which expects the output to be `None`.

`sort_students`

- Empty array and `"math"` as input, which expects the output to be `None`.
- Array with three students and `"history"` as input, which expects the output to be `None`.
- Array with three students and `"math"` as input, which expects the output to be:

```python
[
    {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
    {"name": "Bob", "math": 88, "physics": 79, "chemistry": 95},
    {"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88}
]
```

- Array with three students and `"physics"` as input, which expects the output to be:

```python
[
    {"name": "Bob", "math": 88, "physics": 79, "chemistry": 95},
    {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
    {"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88},
    ]
```

- Array with three students and `"chemistry"` as input, which expects the output to be:

```python
[
    {"name": "Charlie", "math": 92, "physics": 85, "chemistry": 88},
    {"name": "Alice", "math": 75, "physics": 82, "chemistry": 90},
    {"name": "Bob", "math": 88, "physics": 79, "chemistry": 95},
]
```

## Conclusion

All of the implementation of both files were tested and work as intended. All implementation and testing files will be available in the `erg5` folder.
