Here is the Python function to find the last position of an element in a sorted array:

```python
def last(arr, x):
    low = 0
    high = len(arr) - 1
    res = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1

    return res
```

This function uses binary search to find the last occurrence of an element in a sorted array. It initializes two pointers, `low` and `high`, to the start and end of the array respectively. It then enters a loop where it calculates the middle index `mid` and compares the element at `mid` with the target `x`. If the element at `mid` is greater than `x`, it means `x` must be in the left half of the array, so it updates `high` to `mid - 1`. If the element at `mid` is less than `x`, it means `x` must be in the right half of the array, so it updates `low` to `mid + 1`. If the element at `mid` is equal to `x`, it means `x` is found and it updates `res` to `mid` and `low` to `mid + 1` to continue the search in the right half of the array. The loop continues until `low` is greater than `high`. Finally, it returns `res` which is the last position of `x` in the array.
