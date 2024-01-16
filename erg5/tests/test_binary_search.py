from binary_search import binary_search

# Defines test function for binary_search with an empty array as input
def test_binary_search_empty_array():
    array = []
    assert binary_search(array, 1) == -1

# Defines test function for binary_search with an array of length 1
# and an element that exists in the array as input
def test_binary_search_length_1():
    array = [1]
    assert binary_search(array, 1) == 0

# Defines test function for binary_search with a sorted array
# and an element that exists in the array as input
def test_binary_search():
    array = [1, 2, 3, 4, 5]
    assert binary_search(array, 3) == 2

# Defines test function for binary_search with a sorted array
# and an element that does not exist in the array as input
def test_binary_search_not_found():
    array = [1, 2, 3, 4, 5]
    assert binary_search(array, 6) == -1

# Defines test function for binary_search with an unsorted array
# and an element that exists in the array as input
def test_binary_search_unsorted_array():
    array = [3, 2, 5, 1, 4]
    assert binary_search(array, 3) == 2
