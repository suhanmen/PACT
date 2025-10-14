Here is the completed code snippet:

```python
def left_insertion(arr, value):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return left

assert left_insertion([1,2,4,5], 6) == 4
```

This code defines a function `left_insertion` that takes in a sorted array `arr` and a value `value`. It uses a binary search algorithm to find the left insertion point for the specified value in the sorted order. The function returns the index where the value should be inserted.

In the binary search algorithm, we maintain two pointers `left` and `right` that represent the range of indices to search within. We calculate the middle index `mid` and compare the value at that index with the specified value. If the value at `mid` is less than the specified value, we update `left` to `mid + 1` to search in the right half of the array. Otherwise, we update `right` to `mid - 1` to search in the left half of the array. We continue this process until `left` is greater than `right`, indicating that the value should be inserted at `left`.

The provided assertion checks if `left_insertion([1,2,4,5], 6)` returns the expected result of `4`.