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
