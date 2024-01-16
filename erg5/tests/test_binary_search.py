import sys
sys.path.append('../erg5')

from binary_search import binary_search


def test_binary_search_empty_array():
    """
    Defines test function for binary_search with an empty array as input.
    """
    array = []
    assert binary_search(array, 1) == -1

def test_binary_search_one_element_array():
    """
    Defines test function for binary_search with a one-element array
    and an element that exists in the array as input.
    """
    array = [1]
    assert binary_search(array, 1) == 0

def test_binary_search():
    """
    Defines test function for binary_search with a sorted five-element array
    and an element that exists in the array as input.
    """
    array = [1, 2, 3, 4, 5]
    assert binary_search(array, 3) == 2

def test_binary_search_not_found():
    """
    Defines test function for binary_search with a sorted five-element array
    and an element that does not exist in the array as input.
    """
    array = [1, 2, 3, 4, 5]
    assert binary_search(array, 6) == -1
