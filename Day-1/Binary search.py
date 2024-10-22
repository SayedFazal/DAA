'''9. Checks if a given number x exists in a sorted array arr using binary search. Analyze its time complexity using Big-O notation.'''
def binary_search(arr, key):
    arr.sort()  # Sorting the array
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return f"Element {key} is found at position {mid}"
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return f"Element {key} not found"

# Test case
arr = [3, 4, 6, -9, 10, 8, 9, 30]
key = 100
print(binary_search(arr, key))

Output:[-9, 3, 4, 6, 8, 9, 10, 30]
6
