Here is the completed code snippet:

```python
def right_insertion(arr, value):
    """
    Function to locate the right insertion point for a specified value in sorted order.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == value:
            return mid

        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return left

assert right_insertion([1,2,4,5], 6) == 4
```

The `right_insertion` function takes in a sorted array `arr` and a value `value` as parameters. It uses a binary search algorithm to find the right insertion point for the value in the sorted array.

The function initializes two pointers, `left` and `right`, which represent the left and right boundaries of the search range. It then enters a while loop that continues until the left pointer is greater than the right pointer.

Inside the loop, the function calculates the middle index using integer division. It compares the value at the middle index with the target value. If they are equal, it returns the middle index as the right insertion point.

If the value at the middle index is less than the target value, the left pointer is updated to `mid + 1` to search the right half of the array. Otherwise, the right pointer is updated to `mid - 1` to search the left half of the array.

If the loop completes without finding a matching value, the function returns the left pointer as the right insertion point.

The code includes an assertion to verify that the function returns the correct right insertion point for the given example.